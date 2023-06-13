import asyncio

import time

import secterfunction

import automationsectername

from pyppeteer import launch

async def main():
    
    browser = await launch({'headless':False})
    
    page = await browser.newPage()
    
    await page.setViewport({ "width": 1080, "height": 1024 })
    
    await page.goto(automationsectername.facebookurl)
    
    await page.waitForSelector(automationsectername.loginemailselecter)
    
    await page.type(automationsectername.loginemailselecter,automationsectername.loginemail )

    await page.type(automationsectername.loginpasswordselecter,automationsectername.password)

    await page.click(automationsectername.facebooksiginbuttom)
    
    await page.waitForNavigation()
    
    await page.goto(automationsectername.facebookmarketplaceurl)
    
    time.sleep(10)
    
    await page.waitForSelector(automationsectername.facebookmarketplaceselecter)
    
    await page.type(automationsectername.facebookmarketplaceselecter,automationsectername.searchItem)
       
    await page.keyboard.press('Enter')
    
    await secterfunction.autoScroll(page,20000)
    
    time.sleep(10)
    
    await page.waitForSelector(automationsectername.productlinksecter)
    
    productLinks = await secterfunction.selecter_finction(page,automationsectername.productlinksecter)
    
    time.sleep(5)
    
    itemdetailes=[]
    
    for item in productLinks:
        page1 = await browser.newPage()
        
        await page1.goto(item)
        
        await page1.waitForSelector(automationsectername.products_detaiels_secter)
        
        product_detaile =await secterfunction.selecter_finctiontext(page1,automationsectername.products_detaiels_secter)
        
        await page1.waitForSelector(automationsectername.productpriceselecter)
        
        product_price = await secterfunction.selecter_finctiontext(page1,automationsectername.productpriceselecter)
        
        await page1.waitForSelector(automationsectername.product_address_secter)
        
        product_address =await secterfunction.selecter_finctiontext(page1,automationsectername.product_address_secter)
        
        await page1.waitForSelector(automationsectername.product_link)
        
        product_profilelink =await secterfunction.selecter_finction(page1,automationsectername.product_link)
        
        await page1.waitForSelector(automationsectername.product_add_name)
        
        name =await secterfunction.selecter_finctiontext(page1,automationsectername.product_add_name)
        
        result ={
        "DETAILES": product_detaile[0],
        "PRICE":product_price[0],
        "ADDRESS": product_address[0],
        "PRFILE_LINK": product_profilelink[0],
        "NAME":name[0]
        }
        itemdetailes.append(result)
        
        await page1.close()
        
    for data in itemdetailes:
        print(data)
    
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())


