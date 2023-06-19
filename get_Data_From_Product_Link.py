from facebook_selectors import (PRODUCT_DETAILS_SELECTOR,
                               PRODUCT_PRICE_SELECTOR,
                               PRODUCT_ADDRESS_SELECTOR,
                               PRODUCT_ADVERTIS_PROFILE_LINK,
                               PRODUCT_ADVERTIS_PROFILE_NAME)

from get_HrefOrText_OfProduct_Link import GetProductTextOrHref

class DataScraping:

            async def getDataFromProductLink(self, browser, link):
                  
                  newTab = await browser.newPage()
            
                  await newTab.goto(link)
                  
                  await newTab.waitForSelector(PRODUCT_DETAILS_SELECTOR)
                  
                  advertisProductDetails = await GetProductTextOrHref().getInnerText(newTab, PRODUCT_DETAILS_SELECTOR)
                  
                  await newTab.waitForSelector(PRODUCT_PRICE_SELECTOR)
                  
                  advertisProductPrice = await GetProductTextOrHref().getInnerText(newTab, PRODUCT_PRICE_SELECTOR)
                  
                  await newTab.waitForSelector(PRODUCT_ADDRESS_SELECTOR)
                  
                  advertisAddress = await GetProductTextOrHref().getInnerText(newTab, PRODUCT_ADDRESS_SELECTOR)
                  
                  await newTab.waitForSelector(PRODUCT_ADVERTIS_PROFILE_LINK)
                  
                  advertisProfileLink = await GetProductTextOrHref().getHrefLink(newTab, PRODUCT_ADVERTIS_PROFILE_LINK)
                  
                  await newTab.waitForSelector(PRODUCT_ADVERTIS_PROFILE_NAME)
                  
                  avertisProfileName = await GetProductTextOrHref().getInnerText(newTab, PRODUCT_ADVERTIS_PROFILE_NAME)
                  
                  avertisProductAllDetails = {
                        
                        "detailes": advertisProductDetails[0],
                        "price": advertisProductPrice[0],
                        "address": advertisAddress[0],
                        "profile_link": advertisProfileLink[0],
                        "name": avertisProfileName[0]
                        
                  }
                  
                  await newTab.close()
                  
                  return avertisProductAllDetails
                  
                  