from models import *


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    token = Column(String(100), nullable=False, unique=True)
    blog = relationship('Blog')
