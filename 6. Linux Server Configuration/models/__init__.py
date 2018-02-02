from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

__all__ = ['Base', 'relationship', 'Column', 'String', 'Integer', 'DateTime', 'Text', 'ForeignKey']

engine = create_engine('postgresql://catalog:password@localhost/catalogdb', echo=True)

Base = declarative_base()

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


def create_tables():
    Base.metadata.create_all(engine)
