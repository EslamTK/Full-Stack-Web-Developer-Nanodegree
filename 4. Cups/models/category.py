from models import *


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    blog = relationship('Blog')

    @property
    def serialize(self):
        return {
            'category': self.name,
            'blogs': [b.serialize for b in self.blog]
        }
