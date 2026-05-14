from app.pages.BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        self.page = page
        
    def open(self):
        self.page.goto("https://esus.municipio.mg.gov.br/")
        
    def login(self, cpf, password):
        self.fill('#name', cpf)
        self.fill('#password', password)
        self.click('button[type="submit"]') 