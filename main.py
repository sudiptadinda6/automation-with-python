import asyncio

from facebookMarketPlaceWebScraping import WebScraping


asyncio.get_event_loop().run_until_complete(WebScraping().main())