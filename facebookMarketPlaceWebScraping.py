import time

from getHrefOrTextOfProductLink import GetProductTextOrHref

from facebookselectors import (FACEBOOK_URL,
                               FACEBOOK_MARKET_PLACE_URL,
                               emailSelector,
                               EMAILID,
                               passwordSelector,
                               PASSWORD,
                               facebookSigInButton,
                               facebookMarketPlaceSelector,
                               searchItemName,
                               selectAllProductLink)

from getDataFromProductLink import DataScraping


from pyppeteer import launch

class WebScraping:

        async def main(self):
            
            browser = await launch({'headless':False})
            
            page = await browser.newPage()
            
            await page.setViewport({ "width": 1080, "height": 1024 })
            
            await page.goto(FACEBOOK_URL)
            
            await page.waitForSelector(emailSelector)
            
            await page.type(emailSelector, EMAILID )

            await page.type(passwordSelector, PASSWORD)

            await page.click(facebookSigInButton)
            
            await page.waitForNavigation()
            
            await page.goto(FACEBOOK_MARKET_PLACE_URL)
            
            time.sleep(10)
            
            await page.waitForSelector(facebookMarketPlaceSelector)
            
            await page.type(facebookMarketPlaceSelector, searchItemName)
            
            await page.keyboard.press('Enter')
            
            await GetProductTextOrHref().autoScroll(page, 20000)
            
            time.sleep(10)
            
            await page.waitForSelector(selectAllProductLink)
            
            productLinks = await GetProductTextOrHref().getHrefLink(page, selectAllProductLink)
            
            time.sleep(5)
            
            advertisAllProductDetails = []
            
            for link in productLinks:
                
                advertisIndividualProductDetails = await DataScraping().getDataFromProductLink(browser, link)
                
                advertisAllProductDetails.append(advertisIndividualProductDetails)

            await browser.close()
            
            return advertisAllProductDetails




