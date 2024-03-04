from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from fastapi_pagination import add_pagination

from config.config import settings
from mailing.routers import router 


# APP
def create_app() -> FastAPI:
    """
    The application factory using FastAPI framework.
    """

    app = FastAPI(
        title = settings.TITLE_APP,
        version = settings.VERSION_APP,
        debug = settings.DEBUG,
        docs_url = "/docs",
        openapi_url ='/api/openapi.json',
        default_response_class = ORJSONResponse,
        redoc_url = None
    )

    allow_origins: list = [
        'http://0.0.0.0:3000',
        'http://0.0.0.0:8000',
        'http://0.0.0.0:8080',
        'http://0.0.0.0:8888',
        'http://127.0.0.1:8000',
        'http://127.0.0.1:8080',
        'http://127.0.0.1:8888',
        'http://localhost:8000',
        'http://localhost:8080',
        'http://localhost:8888',
        'http://10.28.110.110:8000',
        'https://10.28.110.110:8000',
        'http://10.28.110.110:8080',
        'https://10.28.110.110:8080',
        'http://10.28.110.110:8888',
        'https://10.28.110.110:8888',
        'http://test.mailingbs.rt.ru',
        'https://test.mailingbs.rt.ru',
        'http://mailingbs.rt.ru',
        'https://mailingbs.rt.ru',
    ]

    allow_methods: list = ['OPTIONS', 'HEAD', 'GET', 'POST']

    allow_headers: list = [
        'Content-Type',
        'Set-Cookie',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Credentials',
        'Access-Control-Allow-Origin',  
    ]

    add_pagination(app)
    init_routers(app)
    init_middleware(app, allow_origins, allow_methods, allow_headers)
    return app


def init_routers(app: FastAPI) -> None:
    app.include_router(router, prefix="/api/v1")


def init_middleware(
    app: FastAPI,
    allow_origins: list,
    allow_methods: list,
    allow_headers: list,
) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=False,
        allow_origin_regex=None,
        allow_methods=allow_methods,
        allow_headers=allow_headers
    )
