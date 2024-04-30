#!/usr/bin/python3
'''
write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
'''

import MySQLdb
from sys import argv

if __name__=="__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    query = "SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states\
            WHERE cities.state_id = states.id"
    cursor = db.cursor()
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
