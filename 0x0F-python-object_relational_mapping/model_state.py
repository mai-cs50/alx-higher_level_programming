#!/usr/bin/python3
'''
Write a python file that contains the class definition of a State and an instance Base = declarative_base():
'''

from SQLAlchemy import Column, Integer, String
from SQLAlchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    Base = declarative_base()

    class State(Base):
        '''
        state class
        '''

        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
        name = Column(String(128), nullable=False)
