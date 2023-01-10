import os
import sys
from time import sleep


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
        poll_kwargs: dict[str, str],
):

    consumer = KafkaConsumer(
        data_stream,
        bootstrap_servers=bootstrap_servers,
        value_deserializer=value_deserializer,
        group_id=consumer_group_id,
    )
    while True:
        message = consumer.poll(**poll_kwargs)
        logger.info(f'{message.keys()}')
        sleep(config.KAFKA_MIN_POLL_TIMEOUT_MS / 1000)


if __name__ == "__main__":
    logger = config.factory_logger(__file__)
    handler(
        bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=io.deserialize,
        data_stream=config.KAFKA_STREAM,
        consumer_group_id=config.KAFKA_CONSUMER_GROUP_ID,
        logger=logger,
        poll_kwargs={
            "timeout_ms": config.KAFKA_MAX_POLL_TIMEOUT_MS,
            "max_records": config.KAFKA_POLL_MAX_RECORDS,
        },
    )
