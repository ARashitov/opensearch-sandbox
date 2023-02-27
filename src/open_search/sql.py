from opensearchpy import OpenSearch

from src import config
from src import generators


settings = config.settings
logger = config.logger


def retrieve_filter_sql(client, index: str):
    response = client.transport.perform_request(
        method='POST',
        url='/_plugins/_sql',
        params={"format": "json"},
        body={'query': f"SELECT * FROM {index} WHERE client.application_version = 'v2' LIMIT 5"},
    )
    return response


def aggregate_money_amt(client, index: str):
    QUERY = f"""
        SELECT
            transaction.money.currency_name currency,
            STD(transaction.money.amount) std_amount,
            AVG(transaction.money.amount) avg_amount
        FROM
            {index}
        GROUP BY
            transaction.money.currency_name
    """
    response = client.transport.perform_request(
        method='POST',
        url='/_plugins/_sql',
        params={
            # "format": "csv",
            # "format": "raw",
            # "format": "json",
        },
        body={'query': QUERY},
    )
    return response


if __name__ == "__main__":

    os_client = OpenSearch(
        hosts=settings.opensearch_hosts,
        http_compress=True,
        use_ssl=False,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )

    bets = generators.generate_fake_bets(1)

    results = aggregate_money_amt(os_client, index=settings.index)
    logger.info(results)
