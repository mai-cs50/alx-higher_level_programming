#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''

import MySQLdb
import sys
#from sys import argv

# the code
if __name__ = "__main__":

    # make connection
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    #give
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    #query_rows = cur.fetchall()
    for state in cursor.fetchall():
        print(state)
    #clean
    cursor.close()
    db.close()
