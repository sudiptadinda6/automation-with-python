from facebookselectors import (productDetailsSelector,
                               productPriceSelector,
                               productAddressSelector,
                               productAdvertisProfileLink,
                               productAdvertisprofileName)

from getHrefOrTextOfProductLink import GetProductTextOrHref

class DataScraping:

            async def getDataFromProductLink(self, browser, link):
                  
                  newTab = await browser.newPage()
            
                  await newTab.goto(link)
                  
                  await newTab.waitForSelector(productDetailsSelector)
                  
                  advertisProductDetails = await GetProductTextOrHref().getInnerText(newTab, productDetailsSelector)
                  
                  await newTab.waitForSelector(productPriceSelector)
                  
                  advertisProductPrice = await GetProductTextOrHref().getInnerText(newTab, productPriceSelector)
                  
                  await newTab.waitForSelector(productAddressSelector)
                  
                  advertisAddress = await GetProductTextOrHref().getInnerText(newTab, productAddressSelector)
                  
                  await newTab.waitForSelector(productAdvertisProfileLink)
                  
                  advertisProfileLink = await GetProductTextOrHref().getHrefLink(newTab, productAdvertisProfileLink)
                  
                  await newTab.waitForSelector(productAdvertisprofileName)
                  
                  avertisProfileName = await GetProductTextOrHref().getInnerText(newTab, productAdvertisprofileName)
                  
                  avertisProductAllDetails = {
                  "detailes": advertisProductDetails[0],
                  "price": advertisProductPrice[0],
                  "address": advertisAddress[0],
                  "profile_link": advertisProfileLink[0],
                  "name": avertisProfileName[0]
                  }
                  
                  await newTab.close()
                  
                  return avertisProductAllDetails
                  
                  