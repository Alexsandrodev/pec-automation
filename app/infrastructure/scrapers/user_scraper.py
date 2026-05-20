from pages.gov_login_page import GovLoginPage
from pages.egestor_login_page import EGestorScraper
import asyncio

class UserScraper:
    def __init__(self, browser_manager):
        self.browser = browser_manager
    
    async def scrape(self):
        try: 
            page = await self.browser.new_page()
            
            egestor = EGestorScraper(page)
            
            await egestor.scrape()
            
            gov_login = GovLoginPage(page)
            
            await gov_login.login('091.915.366-69', 'Manu1412')
            
            municipios = await egestor.get_municipios()
            
            return {"municipios": municipios,
                    "quantidade": len(municipios)}
        
        except Exception as e:
                print(f"Ocorreu um erro ({e}), tentando novamente em 3 segundos...")
                
                if page:
                    try:
                        await page.close()
                    except Exception:
                        pass
                
                await asyncio.sleep(3)
                
                dados = await self.scrape()

                return dados
