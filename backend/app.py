import uvicorn

from main import create_app
from config.config import settings


app = create_app()


if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        port = 8000,
        host = settings.HOST,
        reload = settings.RELOAD,
        factory=True
    )
