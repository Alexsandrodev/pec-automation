import re

class EGestorScraper:
    def __init__(self, page):
        self.page = page
        
    async def _open_site(self):
        await self.page.goto("https://acesso-egestoraps.saude.gov.br/login")
        
    async def _go_to_gov_login(self):
        await self.page.locator('xpath=//*[@id="loginForm"]/div[1]/div/div/a').click()
        
    async def get_municipios(self): 
        await self.page.wait_for_url('https://egestorab.saude.gov.br/paginas/acessoRestrito/perfilAcesso.xhtml')
        
        accordion = self.page.locator(
        'xpath=//*[@id="110"]/div/div/div/div[2]/div/div[2]/div[@id="accordion2"]'
        )

        cards = accordion.locator('> div')

        municipios = []

        count = await cards.count()

        for i in range(count):

            nome = await (
                cards
                .nth(i)
                .locator('div:nth-child(1) h4 a strong')
                .text_content()
            )

            nome_limpo = " ".join(nome.split())

            municipios.append(nome_limpo)

        return municipios
    
    async def scrape(self):
        try:
            await self._open_site()
            
            await self._go_to_gov_login()
            
            return True
        
        except Exception as e:
            raise e