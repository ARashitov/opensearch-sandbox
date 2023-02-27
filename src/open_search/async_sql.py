import asyncio

from opensearchpy import OpenSearch
try:
    from opensearchpy._async.transport import AsyncTransport
except ImportError:
    raise RuntimeError("Fail to import AsyncTransport from opensearchpy")

from src import config
# from src import generators


settings = config.settings
logger = config.logger


async def retrieve_filter_sql(client: OpenSearch, index: str):
    response = await client.transport.perform_request(
        method='POST',
        url='/_plugins/_sql',
        params={"format": "json"},
        body={'query': f"SELECT * FROM {index} LIMIT 5"},
    )
    await client.transport.close()
    return response


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    client = OpenSearch(
        hosts=settings.opensearch_hosts,
        transport_class=AsyncTransport,
        http_compress=True,
        use_ssl=True,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )
    response = event_loop.run_until_complete(
        retrieve_filter_sql(client, index=settings.index),
    )
    event_loop.close()
    logger.info(response)
