from models.user import User
from .interfaces.user import UserRepoInterface
from .repo import Repo


class UserRepo(Repo, UserRepoInterface):
    def __init__(self, session):
        super().__init__(session)
        self._entity_type = User

    def get_by_email(self, email):
        user = self._session.query(User).filter(User.email == email).one()
        return user

    def get_by_token(self, token):
        user = self._session.query(User).filter(User.token == token).one()
        return user

    def is_owner_of_blog(self, user, blog):
        return user.id == blog.user_id
