from typing import List
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

root_dir = Path(__file__).parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(root_dir / ".env"), env_file_encoding="utf-8")

    TRONSCAN_API_TOKEN: str
    TRON_ADDRS: List[str]


settings = Settings()
