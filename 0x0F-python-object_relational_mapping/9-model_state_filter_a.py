#!/usr/bin/python3
'''
write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
'''

import MySQLdb
from model_state import Base, State
from SQLAlchemy import creat_engine
from SQLAlchemy.orm import sessionmaker

if __name__=="__main__":
    engine = creat_engine('mysql+mysqldb://{}:{}@localhost/{}'
                          .format(argv[1], argv[2], argv[3]),
                          pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.like('%a%'))
        print("{}: {}".format(state.id, state.name))
    session.close()
