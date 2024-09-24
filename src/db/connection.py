import databases
import ormar
import sqlalchemy
from loguru import logger
from utils import Settings

connections_strings = f"postgresql://" \
                      f"{Settings.PG_USER}:{Settings.PG_PASSWORD}" \
                      f"@{Settings.PG_HOST}:{Settings.PG_PORT}" \
                      f"/{Settings.PG_DB}"
logger.info(connections_strings)
database = databases.Database(
    connections_strings
)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata
