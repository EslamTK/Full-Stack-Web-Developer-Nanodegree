from models.blog import Blog
from models.category import Category
from .interfaces.blog import BlogRepoInterface
from .repo import Repo


class BlogRepo(Repo, BlogRepoInterface):
    def __init__(self, session):
        super().__init__(session)
        self._entity_type = Blog

    def get_by_category(self, category):
        blogs = self._session.query(self._entity_type).join(Category). \
            filter(Category.name == category and
                   self._entity_type.id == Category.id).order_by(self._entity_type.created_at.desc())

        return blogs
