from contextlib import contextmanager
from typing import Generator, Optional, Any, Iterable
from databricks import sql
from loguru import logger


from app.core.config import get_settings


_settings = get_settings()


@contextmanager
def dbx_conn() -> Generator[Any, None, None]:
    conn = None
    try:
        conn = sql.connect(
            server_hostname=_settings.DATABRICKS_SERVER_HOSTNAME,
            http_path=_settings.DATABRICKS_HTTP_PATH,
            access_token=_settings.DATABRICKS_ACCESS_TOKEN,
        )
        yield conn
    finally:
        if conn is not None:
            try:
                conn.close()
            except Exception as e:
                logger.warning(f"Error closing Databricks connection: {e}")


@contextmanager
def dbx_cursor() -> Generator[Any, None, None]:
    with dbx_conn() as conn:
        cursor = conn.cursor()
        try:
            yield cursor
        finally:
            try:
                cursor.close()
            except Exception as e:
                logger.warning(f"Error closing Databricks cursor: {e}")




def fetch_all(query: str, params: Optional[Iterable[Any]] = None) -> list[dict]:
    with dbx_cursor() as cur:
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
            columns = [c[0] for c in cur.description]
            return [dict(zip(columns, row)) for row in cur.fetchall()]




def fetch_one(query: str, params: Optional[Iterable[Any]] = None) -> Optional[dict]:
    with dbx_cursor() as cur:
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        row = cur.fetchone()
        if row is None:
            return None
        columns = [c[0] for c in cur.description]
        return dict(zip(columns, row))




def execute(query: str, params: Optional[Iterable[Any]] = None) -> int:
    """Execute a DML statement (INSERT/UPDATE/DELETE). Returns affected row count if available."""
    with dbx_cursor() as cur:
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        try:
            return cur.rowcount # may be -1 if not supported
        except Exception:
            return -1