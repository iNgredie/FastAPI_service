from pydantic import BaseSettings


class Setting(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = 'sqlite:///./sql_app.db'


settings = Setting(
    _env_file='env',
    _env_file_encoding='utf-8',
)
