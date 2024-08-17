#!/usr/bin/python3
"""
Script to create a State and a City in the hbtn_0e_100_usa database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State
    california = State(name="California")
    # Create a new City associated with the State
    san_francisco = City(name="San Francisco", state=california)

    # Add and commit the new state and city to the database
    session.add(california)
    session.add(san_francisco)
    session.commit()

    session.close()

