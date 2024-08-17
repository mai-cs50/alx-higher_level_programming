#!/usr/bin/python3
"""
Module that defines a State class and creates a table in the database.
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

