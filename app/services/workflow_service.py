from app.models.folder_data import FolderData

class WorkflowService:

    def __init__(
        self,
        login_page,
        folder_page
    ):

        self.login_page = login_page
        self.folder_page = folder_page

    def execute(self):

        self.login_page.open()

        self.login_page.login(
            "admin@email.com",
            "123456"
        )

        folders = [1, 2, 3]

        results = []

        for folder_id in folders:

            self.folder_page.access(folder_id)

            data = FolderData(
                id=folder_id,
                title=self.folder_page.get_title(),
                status=self.folder_page.get_status()
            )

            results.append(
                data.model_dump()
            )

        return results