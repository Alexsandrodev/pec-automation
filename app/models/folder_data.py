from pydantic import BaseModel

class FolderData(BaseModel):
    id: int
    name:str
    status:str