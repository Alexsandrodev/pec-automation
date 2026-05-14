from playwright.async_api import sync_playwright

class BrowserContext:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright.start()
        self.browser = self.playwright.cromium.launch(headless=False)
        
        context = self.browser.new_context()
        
        self.page = context.new_page()
        return self.page
    
    def close(self):
        self.browser.close()
        self.playwright.stop()
        