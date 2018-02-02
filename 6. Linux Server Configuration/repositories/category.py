from models.category import Category
from .interfaces.category import CategoryRepoInterface
from .repo import Repo


class CategoryRepo(Repo, CategoryRepoInterface):
    def __init__(self, session):
        super().__init__(session)
        self._entity_type = Category
