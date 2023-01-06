import logging
KAFKA_BOOTSTRAP_SERVERS = ["localhost:9092"]
KAFKA_STREAM = "bets_to_register"
KAFKA_CONSUMER_GROUP_ID = "bet_registration_consumers"

logging.basicConfig(format='[ %(asctime)s ][ %(levelname)s ]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def factory_logger(fpath: str):
    logger = logging.getLogger(fpath)
    logger.setLevel(logging.INFO)
    return logger
