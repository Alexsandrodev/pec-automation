import asyncio

from infrastructure.browser.playwright_factory import PlaywrightFactory
from infrastructure.browser.browser_manager import BrowserManager
from infrastructure.scrapers.user_scraper import UserScraper
from application.use_cases.scrape_users import ScrapeUsersUseCase

async def main():
    factory = PlaywrightFactory()
    browser = BrowserManager(factory)
    
    await browser.start()
    
    scrape = UserScraper(browser)
    use_case = ScrapeUsersUseCase(scrape)
    results = await use_case.execute()
    
    print(results)
    
    await browser.close()
    
    
if __name__ == "__main__":
    asyncio.run(main())