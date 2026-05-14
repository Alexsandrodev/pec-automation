class FolderPage:
    def __init__(self, page):
        self.page = page
        
    def acess(self, folder_id):
        self.page.goto(f"https://esus.municipio.mg.gov.br/{folder_id}")
        
    def get_title(self):
        return self.page.locator(".folder-title").inner_text()
    
    def get_status(self):
        return self.page.locator(".status").inner_text()