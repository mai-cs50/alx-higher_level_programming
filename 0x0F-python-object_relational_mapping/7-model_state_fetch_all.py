#!/usr/bin/python3
'''
Script that lists all State objects from the database hbtn_0e_6_usa
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the engine and connect to the database
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/
                           {sys.argv[3]}',
                           pool_pre_ping=True)

    # Create the tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to fetch all State objects ordered by id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
