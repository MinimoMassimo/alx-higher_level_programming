#!/usr/bin/python3
'''
lists all cities from database
command-line args: mysql usernmae, password, database name
'''


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM  states
                INNER JOIN cities ON states.id = cities.state_id
                ORDER BY id ASC""")

    for x in cur.fetchall():
        print(x)
    cur.close()
    db.close()
