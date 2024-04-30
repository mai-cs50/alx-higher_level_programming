#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''

import MySQLdb
from sys import argv

# the code
if __name__ == "__main__":
    if len(argv) == 5:
        username, password, database, state_name = argv[1],
        argv[2], argv[3], argv[4]

        # make connection
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])

        # give
        cur = db.cursor()
        me = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
        cur.execute(me)

        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        # clean
        cur.close()
        db.close()
