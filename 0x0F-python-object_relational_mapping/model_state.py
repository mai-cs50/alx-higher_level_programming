#!/usr/bin/python3
"""
Defines a State class and an instance Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

# Create an instance of the Base class
Base = declarative_base()

class State(Base):
    """
    State class that inherits from Base.
    Represents a state in the states table in MySQL.
    """
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Create the engine and connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )
    
    # Create all tables in the engine
    Base.metadata.create_all(engine)

