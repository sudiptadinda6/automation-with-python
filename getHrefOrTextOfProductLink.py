class GetProductTextOrHref:

        async def getHrefLink(self, page, selectorUse):

            return await page.evaluate('''(sel) => {
                const elements = document.querySelectorAll(sel);
                return Array.from(elements, (el) => el.href);
            }''', selectorUse)
            


        async def getInnerText(self, page, selectorUse):

            return await page.evaluate('''(sel) => {
                const elements = document.querySelectorAll(sel);
                return Array.from(elements, (el) => el.innerText);
            }''', selectorUse)
            

        async def autoScroll(self, page, newValue):
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
           }''', newValue)