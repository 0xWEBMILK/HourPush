import aiohttp

async def action(base_url: str, token: str, event: str, *args) -> dict:
    """
    Sends an asynchronous GET request to a specified URL using aiohttp and returns the JSON response.

    Args:
        base_url (str): The base URL of the API endpoint.
        token (str): The authentication token for the API.
        event (str): The event or resource endpoint to be accessed.
        *args: Additional optional arguments for the request (not used in this function).

    Returns:
        dict: The JSON response from the API.
    
    Raises:
        aiohttp.ClientResponseError: If the HTTP response status is not 200.
    """
    url = f"https://{base_url}/{token}/{event}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            
            if response.status != 200:
                response.raise_for_status()

            return await response.json()
