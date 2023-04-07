from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from core.config import app_config
from routers.message import router as message_router
from routers.root import router as root_router
from routers.user import router as user_router


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

app.include_router(message_router, prefix="/api/v1/message", tags=["Message"])
app.include_router(root_router, prefix="/api/v1/root", tags=["Root"])
app.include_router(user_router, prefix="/api/v1/users", tags=["User"])


if __name__ == '__main__':
    run(
        'main:app',
        port = app_config.PORT,
        host = app_config.HOST,
        reload = app_config.DEBUG
    )
