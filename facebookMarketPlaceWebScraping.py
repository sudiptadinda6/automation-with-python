import time

from getHrefOrTextOfProductLink import GetProductTextOrHref

import selectorName 

from getDataFromProductLink import DataScraping


from pyppeteer import launch

class WebScraping:

        async def main(self):
            
            browser = await launch({'headless':False})
            
            page = await browser.newPage()
            
            await page.setViewport({ "width": 1080, "height": 1024 })
            
            await page.goto(selectorName.facebookUrl)
            
            await page.waitForSelector(selectorName.emailSelector)
            
            await page.type(selectorName.emailSelector , selectorName.emailId)

            await page.type(selectorName.passwordSelector , selectorName.password)

            await page.click(selectorName.facebookSigInButton)
            
            await page.waitForNavigation()
            
            await page.goto(selectorName.facebookMarketPlaceUrl)
            
            time.sleep(10)
            
            await page.waitForSelector(selectorName.facebookMarketPlaceSelector)
            
            await page.type(selectorName.facebookMarketPlaceSelector , selectorName.searchItemName)
            
            await page.keyboard.press('Enter')
            
            await GetProductTextOrHref().autoScroll(page , 20000)
            
            time.sleep(10)
            
            await page.waitForSelector(selectorName.selectAllProductLink)
            
            productLinks = await GetProductTextOrHref().getHrefLink(page , selectorName.selectAllProductLink)
            
            time.sleep(5)
            
            advertisAllProductDetails = []
            
            for link in productLinks:
                
                newTab = await browser.newPage()
                
                advertisIndividualProductDetails = await DataScraping().getDataFromProductLink(newTab, link)
                
                advertisAllProductDetails.append(advertisIndividualProductDetails)
                
                
            for data in advertisAllProductDetails:
                print(data)
            
            await browser.close()




