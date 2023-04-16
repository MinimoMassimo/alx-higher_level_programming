#!/usr/bin/python3
'''
contains clas definition fo State and an instance Base
'''


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    Class state - instance of base
    Linked to sql table 'states'
    '''
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
