from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from functools import lru_cache
from app.core.config import get_settings


_settings = get_settings()

HOST = _settings.DATABRICKS_SERVER_HOSTNAME
HTTP_PATH = _settings.DATABRICKS_HTTP_PATH
TOKEN = _settings.DATABRICKS_ACCESS_TOKEN
CATALOG = _settings.DATABRICKS_CATALOG


SessionFactory = sessionmaker(autoflush=False, autocommit=False)

def _build_url(schema: str) -> str:
    # Databricks SQLAlchemy URL format; schema is supplied per request
    return (
        f"databricks://token:{TOKEN}@{HOST}"
        f"?http_path={HTTP_PATH}&catalog={CATALOG}&schema={schema}"
    )

@lru_cache(maxsize=32)
def get_engine(schema: str) -> Engine:
    """
    Return a cached SQLAlchemy Engine for the given schema.
    Engines are safe to cache and share; sessions are not.
    """
    url = _build_url(schema)
    return create_engine(url, echo=False, future=True)

def get_session(schema: str) -> Generator[Session, None, None]:
    """
    FastAPI dependency: supply `schema` as a path or query parameter,
    and this dependency will create/close a Session bound to that schema.
    """
    engine = get_engine(schema)
    db: Session = SessionFactory(bind=engine)
    try:
        yield db
    finally:
        db.close()