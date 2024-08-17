#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Ensure there are exactly 3 arguments (excluding the script name)
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Get the MySQL username, password, and database name from the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine that connects to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}",
        pool_pre_ping=True
    )

    # Create all tables in the engine (if not already created)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object by id
    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()

