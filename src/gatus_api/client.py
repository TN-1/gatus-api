import asyncio
from typing import Any
import aiohttp

class GatusClientError(Exception):
    """Base exception for Gatus Client."""
    pass

class GatusClient:
    """Asynchronous client for interacting with the Gatus API."""

    def __init__(self, url: str, session: aiohttp.ClientSession) -> None:
        self.url = url.rstrip("/")
        self.session = session

    async def get_endpoints_statuses(self) -> list[dict[str, Any]]:
        """Fetch endpoint statuses from Gatus."""
        api_url = f"{self.url}/api/v1/endpoints/statuses"
        try:
            async with asyncio.timeout(10):
                async with self.session.get(api_url) as response:
                    if response.status != 200:
                        raise GatusClientError(
                            f"Gatus API returned status code {response.status}"
                        )
                    
                    data = await response.json()
                    if not isinstance(data, list):
                        raise GatusClientError(
                            "Gatus API response was not in the expected array format"
                        )
                    return data
        except (aiohttp.ClientError, TimeoutError) as err:
            raise GatusClientError(f"Error communicating with Gatus API: {err}") from err
