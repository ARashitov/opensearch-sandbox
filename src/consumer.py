import os
import sys

from kafka import KafkaConsumer

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.shared import io  # noqa: I100,E402
from src import config  # noqa: I100,E402


def handler(
        bootstrap_servers: list[str],
        value_deserializer: callable,
        data_stream: str,
        consumer_group_id: str,
        logger: object,
):

    consumer = KafkaConsumer(
        data_stream,
        bootstrap_servers=bootstrap_servers,
        value_deserializer=value_deserializer,
        group_id=consumer_group_id,
    )

    for message in consumer:
        logger.info(f'{message.value}')


if __name__ == "__main__":
    logger = config.factory_logger(__file__)
    handler(
        bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=io.deserialize,
        data_stream=config.KAFKA_STREAM,
        consumer_group_id=config.KAFKA_CONSUMER_GROUP_ID,
        logger=logger,
    )
