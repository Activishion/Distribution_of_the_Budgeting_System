from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from core.config import app_config


app = FastAPI(
    title = app_config.APP_TITLE,
    description = app_config.APP_DESCRIPTION,
    version = app_config.APP_VERSION,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins='origins_host',
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
    allow_headers=[
        'Content-Type',
        'Set-Cookie',
        'Access-Control-Allow-Headers',
        'Authorization'
    ],
)


origins_host = [
    'http://localhost:8000'
]


if __name__ == '__main__':
    run(
        'main:app',
        port = app_config.PORT,
        host = app_config.HOST,
        reload = app_config.DEBUG
    )
