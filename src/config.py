import logging


KAFKA_BOOTSTRAP_SERVERS = ["localhost:9092"]
KAFKA_STREAM = "bets_to_register"
KAFKA_CONSUMER_GROUP_ID = "bet_registration_consumers"
KAFKA_MIN_POLL_TIMEOUT_MS = 1000
KAFKA_MAX_POLL_TIMEOUT_MS = 2000
KAFKA_POLL_MAX_RECORDS = 20000
KAFKA_PRODUCER_SLEEP_SEC = 0.4

logging.basicConfig(format='[ %(asctime)s ][ %(levelname)s ]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def factory_logger(fpath: str):
    logger = logging.getLogger(fpath)
    logger.setLevel(logging.INFO)
    return logger
