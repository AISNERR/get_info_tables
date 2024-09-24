import contextlib
from fastapi import FastAPI, status
from db.connection import BaseMeta


def create_fastapi_app():
    @contextlib.asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.database = BaseMeta.database
        try:
            database_ = app.state.database
            if not database_.is_connected:
                await database_.connect()
            yield
        finally:
            database_ = app.state.database
            if not database_.is_connected:
                await database_.connect()

    app = FastAPI(lifespan=lifespan)

    return app


app = create_fastapi_app()
