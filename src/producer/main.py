from time import sleep

from kafka import KafkaProducer

from .bet_generator import BetGenerator


def handler(
        bootstrap_servers: list[str],
        value_serializer: callable,
        data_stream: str,
        logger: object,
        producer_sleep_sec: int,
):

    def success_callback(record):
        logger.info(f"Succesfull :: topic={record.topic}&partition={record.partition}&offset={record.offset}")

    def fail_callback(record):
        logger.info(f"Fail :: topic={record.topic}&partition={record.partition}&offset={record.offset}")

    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=value_serializer,
    )
    bet_generator = BetGenerator()

    while (True):
        sleep(producer_sleep_sec)
        producer \
            .send(data_stream, bet_generator.generate()) \
            .add_callback(success_callback) \
            .add_errback(fail_callback)
