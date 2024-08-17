#!/usr/bin/python3
"""
Defines the City class for SQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State

class City(Base):
    """
    Represents the cities table in the database.
    """
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    
    # Establish relationship with the State class
    state = relationship("State", back_populates="cities")

# Ensure `Base` has a `cities` attribute
State.cities = relationship("City", back_populates="state")

