#!/usr/bin/python3
'''
list all cities of given state
command-line args: mysql username, password, db, state name
'''


import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM states INNER JOIN cities
                ON states.id=cities.state_id
                WHERE states.name LIKE %s ORDER BY cities.id ASC""", [argv[4]])

    print(', '.join(["{:s}".format(x[0]) for x in cur.fetchall()]))
    cur.close()
    db.close()
