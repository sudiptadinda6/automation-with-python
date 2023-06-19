import time

from get_HrefOrText_OfProduct_Link import GetProductTextOrHref

from facebook_selectors import (FACEBOOK_URL,
                                FACEBOOK_MARKET_PLACE_URL,
                                EMAIL_SELECTOR,
                                EMAILID,
                                PASSWORD_SELECTOR,
                                PASSWORD,
                                FACEBOOK_SIGIN_BUTTON_SELECTOR,
                                FACEBOOK_MARKETPLACE_SELECTOR,
                                SEARCH_ITEM_NAME,
                                SELECT_ALL_PRODUCT_LINK)

from get_Data_From_Product_Link import DataScraping


from pyppeteer import launch

class WebScraping:

        async def main(self):
            
            browser = await launch({'headless':False})
            
            page = await browser.newPage()
            
            await page.setViewport({ "width": 1080, "height": 1024 })
            
            await page.goto(FACEBOOK_URL)
            
            await page.waitForSelector(EMAIL_SELECTOR)
            
            await page.type(EMAIL_SELECTOR, EMAILID )

            await page.type(PASSWORD_SELECTOR, PASSWORD)

            await page.click(FACEBOOK_SIGIN_BUTTON_SELECTOR)
            
            await page.waitForNavigation()
            
            await page.goto(FACEBOOK_MARKET_PLACE_URL)
            
            time.sleep(10)
            
            await page.waitForSelector(FACEBOOK_MARKETPLACE_SELECTOR)
            
            await page.type(FACEBOOK_MARKETPLACE_SELECTOR, SEARCH_ITEM_NAME)
            
            await page.keyboard.press('Enter')
            
            await GetProductTextOrHref().autoScroll(page, 20000)
            
            time.sleep(10)
            
            await page.waitForSelector(SELECT_ALL_PRODUCT_LINK)
            
            productLinks = await GetProductTextOrHref().getHrefLink(page, SELECT_ALL_PRODUCT_LINK)
            
            time.sleep(5)
            
            advertisAllProductDetails = []
            
            for link in productLinks:
                
                advertisIndividualProductDetails = await DataScraping().getDataFromProductLink(browser, link)
                
                advertisAllProductDetails.append(advertisIndividualProductDetails)

            await browser.close()
            
            return advertisAllProductDetails




