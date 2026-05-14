from playwright.sync_api import Page
from loguru import logger

class BasePage:

    def __init__(self, page: Page):

        self.page = page

    def click(self, element: str):

        try:
            locator = self.page.locator(element)
            locator = wait_for(timeout=10000)
            locator.click()
        except Exception as error:
            self.page.screenshot(path="error.png")
            raise error

    def fill(self, element: str, value: str):

        logger.info(f"Filling: {element}")

        self.page.locator(element).fill(value)

    def goto(self, url: str):

        logger.info(f"Accessing URL: {url}")

        self.page.goto(url)