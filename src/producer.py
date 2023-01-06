import os
import sys

from src import config
from src.producer.main import handler
from src.shared import io


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


if __name__ == "__main__":
    logger = config.factory_logger(__file__)
    handler(
        bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=io.serialize,
        data_stream=config.KAFKA_STREAM,
        logger=logger,
    )
