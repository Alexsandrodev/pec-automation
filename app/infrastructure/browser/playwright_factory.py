from playwright.async_api import async_playwright

class PlaywrightFactory:
    async def create(self):
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(
            headless=False,
            slow_mo=300, 
            args=["--disable-blink-features=AutomationControlled"])
        
        return playwright, browser