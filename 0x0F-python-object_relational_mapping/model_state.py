#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# import sys

# argv = sys.argv
# engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key =True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
