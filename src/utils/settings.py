from dotenv import load_dotenv
from environs import Env

load_dotenv()
env = Env()


class Settings:
    PG_HOST = env.str("PG_HOST", "0.0.0.0")
    PG_PORT = env.int("PG_PORT", 5432)
    PG_USER = env.str("PG_USER", "events")
    PG_PASSWORD = env.str("PG_PASSWORD", "12345")
    PG_DB = env.str("PG_DB", "events")
    UVICORN_PORT = env.int("UVICORN_PORT", 5555)
    UVICORN_HOST = env.str("UVICORN_HOST", "0.0.0.0")