import asyncio

from facebookMarketPlaceWebScraping import WebScraping


data = asyncio.get_event_loop().run_until_complete(WebScraping().main())

for item in data:
    print(item)