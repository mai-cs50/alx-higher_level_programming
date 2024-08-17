#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./10-model_state_my_get.py <mysql username> "
              "<mysql password> <database name> <state name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/"
        f"{database_name}",
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query state by name, safely using parameters
    state = session.query(State).filter(State.name == state_name).first()
    
    if state:
        print(state.id)
    else:
        print("Not fo

