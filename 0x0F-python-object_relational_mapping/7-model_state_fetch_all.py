#!/usr/bin/python3
'''
write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
'''

import sys import argv
from model_state import Base, State
from SQLAlchemy import creat_engine
from SQLAlchemy.orm import sessionmaker

if __name__ == "__main__":
    #create_engine
    engine = creat_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
                          pool_pre_ping=True)
    Base.metadata.creat_all(engine)
    #creat
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(state).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
