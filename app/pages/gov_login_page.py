class GovLoginPage:
    def __init__(self, page):
        self.page = page
        
    async def login(self, cpf: str, password: str):   
        try: 
            await self.page.locator('input[name="accountId"]').fill(cpf)
            
            await self.page.locator('//*[@id="enter-account-id"]').click()
            
            await self.page.locator('input[name="password"]').fill(password)
            
            await self.page.locator('//*[@id="submit-button"]').click()
        except Exception as e:
            return False
        