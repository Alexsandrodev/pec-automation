class ScrapeUsersUseCase:
    def __init__(self, scraper):
        self.scraper =  scraper
        
    async def execute(self):
        data = await self.scraper.scrape()
        
        return data