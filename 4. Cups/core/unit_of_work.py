from models import session
from repositories.blog import BlogRepo
from repositories.category import CategoryRepo
from repositories.user import UserRepo


class UnitOfWork:
    def __init__(self):
        self._blogs = BlogRepo(session)
        self._categories = CategoryRepo(session)
        self._users = UserRepo(session)

    def get_users(self):
        return self._users

    def get_blogs(self):
        return self._blogs

    def get_categories(self):
        return self._categories

    def save(self):
        session.commit()
