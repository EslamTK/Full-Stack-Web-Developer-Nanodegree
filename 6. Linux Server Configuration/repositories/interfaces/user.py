from abc import ABC, abstractmethod


class UserRepoInterface(ABC):
    @abstractmethod
    def get_by_email(self, email):
        pass

    @abstractmethod
    def get_by_token(self, token):
        pass

    @abstractmethod
    def is_owner_of_blog(self, user, blog):
        pass
