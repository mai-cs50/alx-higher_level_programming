#!/usr/bin/python3
"""
Fetches all City objects from the database hbtn_0e_14_usa
and prints them in the format: <state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine and bind it to the Base class
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to fetch all cities and their corresponding states
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Print results in the required format
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()

