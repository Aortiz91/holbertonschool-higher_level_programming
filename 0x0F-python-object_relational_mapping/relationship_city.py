#!/usr/bin/python3
""" Module that contains the class definition of a City and an instance
    Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class defining City table"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
