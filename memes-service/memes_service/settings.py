from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HOST: str = '0.0.0.0'
    PORT: int = 8000

    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_USER: str = 'postgres'
    DB_PWD: str = 'postgres'
    DB_NAME: str = 'postgres2'

    MINIO_ENDPOINT: str = 'localhost'
    MINIO_ACCESS_KEY: str = 'miniominio'
    MINIO_SECRET_KEY: str = 'miniominio'

    @property
    def DATABASE_URL(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PWD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


SETTINGS = Settings()
