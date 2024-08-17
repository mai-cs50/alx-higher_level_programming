#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create the engine and session
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}",
        pool_pre_ping=True
    )
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query state by name
    state = session.query(State).filter(State.name == state_name).first()
    
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()

if __name__ == "__main__":
    main()
