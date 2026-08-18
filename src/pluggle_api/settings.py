from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

PACKAGE_ROOT = Path(__file__).resolve().parent
RUNTIME_ROOT = Path.cwd()

ENV_FILE = RUNTIME_ROOT / ".env"

STATIC_DIR = PACKAGE_ROOT / "static"
TEMPLATES_DIR = PACKAGE_ROOT / "templates"


class Settings(BaseSettings):
    app_env: str
    debug: bool
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int
    host: str
    port: int
    allowed_source_hosts: str

    model_config = SettingsConfigDict(env_file=str(ENV_FILE))

    @computed_field
    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )
