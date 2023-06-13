async def selecter_finction(page,selecteruse):

    productLinks = await page.evaluate('''(sel) => {
        const elements = document.querySelectorAll(sel);
        return Array.from(elements, (el) => el.href);
    }''',selecteruse)
    
    return productLinks


async def selecter_finctiontext(page,selecteruse):

    data = await page.evaluate('''(sel) => {
        const elements = document.querySelectorAll(sel);
        return Array.from(elements, (el) => el.innerText);
    }''',selecteruse)
    
    return data

async def autoScroll(page,newValue):
    await page.evaluate('''async (newValue) => {
        await new Promise((resolve) => {
            var totalHeight = 0;
            var distance = 100;
            var timer = setInterval(() => {
                var scrollHeight = document.body.scrollHeight;
                window.scrollBy(0, distance);
                totalHeight += distance;

                if((newValue && totalHeight>=newValue)||(totalHeight >=scrollHeight -window.innerHeight)){
                    clearInterval(timer);
                    resolve();
                }
            }, 100);
        });
    }''',newValue)