from abc import ABC, abstractmethod

class Browser(ABC):
    @abstractmethod
    async def new_page(self):
        pass