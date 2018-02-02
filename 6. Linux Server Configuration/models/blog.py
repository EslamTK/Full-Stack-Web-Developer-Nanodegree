import datetime

from models import *
from models.category import Category
from models.user import User


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id))
    user_id = Column(Integer, ForeignKey(User.id))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }
