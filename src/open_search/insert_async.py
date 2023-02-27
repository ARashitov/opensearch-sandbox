import asyncio
import aiohttp
import requests

from src import config
from src.decorators import timeit
from src.generators.bet import BetGenerator


settings = config.settings
logger = config.logger


@timeit
def sync_insert(bets: list[dict], settings: config.Settings) -> list[dict]:

    response = []
    auth = requests.auth.HTTPBasicAuth(*settings.opensearch_basic_auth)

    with requests.Session() as session:
        for bet in bets:
            r = session.post(
                url=f"{settings.opensearch_url}{settings.index}/_doc",
                json=bet,
                auth=auth,
                verify=False,
            )
            response.append(r.json())
    return response


async def ingest(url, bet, session, auth: aiohttp.BasicAuth):
    async with session.post(url, json=bet, auth=auth, verify_ssl=False) as response:
        return await response.json()


@timeit
async def async_insert(bets: list[dict], settings: config.Settings):

    url = f"{settings.opensearch_url}{settings.index}/_doc"

    futures = []
    auth = aiohttp.BasicAuth(*settings.opensearch_basic_auth)
    async with aiohttp.ClientSession() as session:

        for bet in bets:
            future = asyncio.ensure_future(ingest(url, bet, session, auth))
            futures.append(future)

        responses = await asyncio.gather(*futures)

    return responses


if __name__ == "__main__":
    bet_generator = BetGenerator()
    bets = [
        bet_generator.generate()
        for bet_id in range(settings.amt_bets_to_generate)
    ]
    # responses = sync_insert(bets, settings=settings)

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(async_insert(bets, settings=settings))
    responses = loop.run_until_complete(future)

    logger.info(responses[0])
