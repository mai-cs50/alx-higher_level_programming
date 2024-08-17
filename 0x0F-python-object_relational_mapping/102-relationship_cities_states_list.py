#!/usr/bin/python3
"""
Script to list all City objects from the hbtn_0e_101_usa database,
along with their corresponding State names.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./102-relationship_cities_states_list.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all cities with their state
    cities = session.query(City).order_by(City.id).all()

    # Display cities and their states
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()

