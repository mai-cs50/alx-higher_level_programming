#!/usr/bin/python3
"""
Definition of the State class that inherits from Base.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City, Base

class State(Base):
    """
    State class that represents the states table.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    
    # Relationship to City, with cascade delete
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

