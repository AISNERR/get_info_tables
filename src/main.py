import asyncio
from signal import SIGINT, SIGTERM
from loguru import logger
from uvicorn import Config, Server
from api import api_routing
from app.app import app
from utils import Settings


def build_app():
    app.include_router(api_routing.router)
    return app


app_assembled = build_app()


async def main(loop: asyncio.AbstractEventLoop) -> None:
    application = app_assembled
    config = Config(
        app=application,
        loop=loop,
        port=int(Settings.UVICORN_PORT),
        host=Settings.UVICORN_HOST.__str__()
    )
    server = Server(config)
    try:
        run_server = loop.create_task(server.serve())
        await asyncio.gather(
            run_server
        )
    except asyncio.CancelledError:
        logger.info("Caught keyboard interrupt. Canceling tasks...")


if __name__ == '__main__':
    event_loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    main_task = asyncio.ensure_future(
        main(
            loop=event_loop
        )
    )
    for signal in [
        SIGINT,
        SIGTERM
    ]:
        event_loop.add_signal_handler(
            signal,
            main_task.cancel
        )
    try:
        event_loop.run_until_complete(
            main_task
        )
    finally:
        event_loop.close()
        logger.info("All tasks stop. Graceful shutdown succeed")