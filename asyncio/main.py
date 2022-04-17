import asyncio

import aiohttp

API_ENDPOINT = 'https://swapi.dev/api/people'

MAX_CHUNK = 10


async def get_person(person_id: int) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{API_ENDPOINT}/{person_id}') as response:
            response = await response.json()
            return response


async def main():
    result = await asyncio.gather(*[get_person(i) for i in range(1, 10)])
    print(result)


asyncio.run(main())
