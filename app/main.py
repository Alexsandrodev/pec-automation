from app.core.browser import BrowserManager

from app.pages.login_page import LoginPage
from app.pages.folder_page import FolderPage

from app.services.workflow_service import WorkflowService

def main():

    browser = BrowserManager()

    page = browser.start()

    try:

        login_page = LoginPage(page)

        folder_page = FolderPage(page)

        workflow = WorkflowService(
            login_page,
            folder_page
        )

        data = workflow.execute()

        print(data)

    finally:

        browser.close()

if __name__ == "__main__":
    main()