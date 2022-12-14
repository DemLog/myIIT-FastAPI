from typing import List, Optional, Dict, Any
from pydantic import BaseSettings, AnyHttpUrl, validator, PostgresDsn


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    # SERVER_NAME: str
    # SERVER_HOST: AnyHttpUrl
    #
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    #
    # @validator("BACKEND_CORS_ORIGINS", pre=True)
    # def assemble_cors_origins(cls, v: str | List[str]) -> List[str] | str:
    #     if isinstance(v, str) and not v.startswith("["):
    #         return [i.strip() for i in v.split(",")]
    #     elif isinstance(v, (list, str)):
    #         return v
    #     raise ValueError(v)

    PROJECT_NAME: str = "myIIT"

    # Настройки БД
    POSTGRES_SERVER: str = "localhost:55000"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgrespw"
    POSTGRES_DB: str = "myIIT"
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True


settings = Settings()
