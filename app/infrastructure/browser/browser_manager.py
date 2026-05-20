class BrowserManager:
    def __init__(self, factory):
        self._factory = factory
        self._playwright = None
        self.browser = None
        self.context = None
        
    async def start(self):
        self._playwright, self.browser = await self._factory.create()
        self.context = await self.browser.new_context(
            locale="pt-BR",
            timezone_id="America/Sao_paulo",
            ignore_https_errors=True,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
        )
    
    async def new_page(self):
        return await self.browser.new_page()
    
    async def close(self):
        await self.context.close()
        await self.browser.close()
        await self._playwright.stop()