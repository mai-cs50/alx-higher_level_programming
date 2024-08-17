#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if there are exactly 3 arguments (excluding the script name)
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <mysql username> "
              "<mysql password> <database name>")
        sys.exit(1)

    # Extract MySQL username, password, and database name from arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine that connects to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/"
        f"{database_name}",
        pool_pre_ping=True
    )

    # Create all tabl
