from abc import ABC, abstractmethod


class BlogRepoInterface(ABC):
    @abstractmethod
    def get_by_category(self, category):
        pass
