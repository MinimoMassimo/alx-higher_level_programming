#!/usr/bin/python3
"""
return all states from database 'hbtn_0e_0_usa
parameters passed: username, password, database
"""


import MySQLdb
from sys import argv

if __name__=="__main__":


    #connect to database:
    DB = MySQLdb.connect(host='localhost', port=3306,
            user=argv[1], passwd=argv[2],
            db=argv[3])

    #create cursor to execute SQL queries
    cur = DB.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for x in cur.fetchall():
        print(x)
    cur.close()
    DB.close()
