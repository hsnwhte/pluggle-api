from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).parent.parent.parent
ENV_FILE = PROJECT_ROOT / ".env"
STATIC_DIR = PROJECT_ROOT / "src" / "pluggle_api" / "static"
TEMPLATES_DIR = PROJECT_ROOT / "src" / "pluggle_api" / "templates"


class Settings(BaseSettings):
    app_env: str
    debug: bool
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: str
    database_url: str
    host: str
    port: int
    allowed_source_hosts: str

    model_config = SettingsConfigDict(env_file=str(ENV_FILE))
