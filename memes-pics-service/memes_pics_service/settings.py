from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ACCESS_ENDPOINT: str = 'http://localhost/imgs'

    HOST: str = '0.0.0.0'
    PORT: int = 8000

    MINIO_ENDPOINT: str = 'localhost'
    MINIO_ACCESS_KEY: str = 'miniominio'
    MINIO_SECRET_KEY: str = 'miniominio'


SETTINGS = Settings()
