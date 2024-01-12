#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''
import MySQLdb
from sys import argv

# the code
if __name__ = "__main__":

    # make connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    #give
    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    #clean
    cur.close()
    db.close()
