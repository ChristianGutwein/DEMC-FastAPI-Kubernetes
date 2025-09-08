from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)

    # App
    APP_NAME: str = Field(default="fastapi-dbx")
    APP_ENV: str = Field(default="local")
    APP_DEBUG: bool = Field(default=True)
    APP_HOST: str = Field(default="0.0.0.0")
    APP_PORT: int = Field(default=8000)


    # Databricks
    DATABRICKS_SERVER_HOSTNAME: str
    DATABRICKS_HTTP_PATH: str
    DATABRICKS_ACCESS_TOKEN: str


    DATABRICKS_CATALOG: str = Field(default="mhpdeworkshop_databricks")
    DATABRICKS_SCHEMA: str = Field(default="00_juewei_silver")
    DATABRICKS_TABLE: str = Field(default="nyc_taxi_enriched")


@lru_cache
def get_settings() -> Settings:
    return Settings()