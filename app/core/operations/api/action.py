import aiohttp

async def action(base_url, token, event, *args):
    url = f"https://{base_url}/{token}/{event}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            
            if response.status != 200:
                response.raise_for_status()

            return await response.json()