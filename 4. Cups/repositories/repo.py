from .interfaces.repo import RepoInterface


class Repo(RepoInterface):
    def __init__(self, session):
        self._session = session
        self._entity_type = None

    def add(self, entity):
        self._session.add(entity)

    def delete(self, entity):
        self._session.delete(entity)

    def get_by_id(self, entity_id):
        return self._session.query(self._entity_type).filter(self._entity_type.id == entity_id).one()

    def get_all(self):
        return self._session.query(self._entity_type).all()
