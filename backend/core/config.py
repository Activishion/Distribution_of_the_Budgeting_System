from os import environ

from pydantic import BaseSettings


class AppConfig(BaseSettings):
    APP_TITLE: str = 'Рассылка Системы бюджетирования.'
    APP_DESCRIPTION: str = 'Рассылка Системы бюджетирования.'
    APP_VERSION: str = '0.1'

    """ db """
    DB_USER = environ.get("DB_USER", str)
    DB_PASSWORD = environ.get("DB_PASSWORD", str)
    DB_HOST = environ.get("DB_HOST", str)
    DB_PORT = environ.get("DB_PORT", str)
    DB_NAME = environ.get("DB_NAME", str)

    """ deploy """
    PORT = environ.get("PORT", str)
    HOST = environ.get("HOST", str)
    DEBUG: bool = True


app_config = AppConfig()