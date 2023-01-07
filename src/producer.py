import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src import config  # noqa: I100,E402
# pylint: disable-next=E0611
from src.producer.main import handler  # noqa: I100,E402
from src.shared import io  # noqa: I100,E402


if __name__ == "__main__":
    logger = config.factory_logger(__file__)
    handler(
        bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=io.serialize,
        data_stream=config.KAFKA_STREAM,
        logger=logger,
        producer_sleep_sec=config.KAFKA_PRODUCER_SLEEP_SEC,
    )
