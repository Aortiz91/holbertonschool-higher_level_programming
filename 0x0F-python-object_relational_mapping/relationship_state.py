#!/usr/bin/python3
""" Module that contains the class definition of a State and an instance
    Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """Class defining state table"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete-orphan",
                          backref='states')
