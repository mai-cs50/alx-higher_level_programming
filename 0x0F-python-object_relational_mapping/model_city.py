#!/usr/bin/python3
"""
Module to define the City class for SQLAlchemy ORM.

The City class represents the 'cities' table in the database and has
a relationship with the 'states' table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """
    Represents a city in the 'cities' table.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State')

