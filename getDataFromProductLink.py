import selectorName

from getHrefOrTextOfProductLink import GetProductTextOrHref

class DataScraping:

            async def getDataFromProductLink(self,newTab,link):
            
                  await newTab.goto(link)
                  
                  await newTab.waitForSelector(selectorName.productDetailsSelector)
                  
                  advertisProductDetails = await GetProductTextOrHref().getInnerText(newTab , selectorName.productDetailsSelector)
                  
                  await newTab.waitForSelector(selectorName.productPriceSelector)
                  
                  advertisProductPrice = await GetProductTextOrHref().getInnerText(newTab , selectorName.productPriceSelector)
                  
                  await newTab.waitForSelector(selectorName.productAddressSelector)
                  
                  advertisAddress = await GetProductTextOrHref().getInnerText(newTab , selectorName.productAddressSelector)
                  
                  await newTab.waitForSelector(selectorName.productAdvertisProfileLink)
                  
                  advertisProfileLink = await GetProductTextOrHref().getHrefLink(newTab , selectorName.productAdvertisProfileLink)
                  
                  await newTab.waitForSelector(selectorName.productAdvertisprofileName)
                  
                  avertisProfileName = await GetProductTextOrHref().getInnerText(newTab , selectorName.productAdvertisprofileName)
                  
                  avertisProductAllDetails ={
                  "detailes": advertisProductDetails[0],
                  "price":advertisProductPrice[0],
                  "address": advertisAddress[0],
                  "profile_link": advertisProfileLink[0],
                  "name":avertisProfileName[0]
                  }
                  
                  await newTab.close()
                  
                  return avertisProductAllDetails
                  
                  