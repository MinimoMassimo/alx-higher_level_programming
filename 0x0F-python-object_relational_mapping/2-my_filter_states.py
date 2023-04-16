#!/usr/bin/python3
'''
displays all values in states table of hbtn_0e_0_usa
command-line arg - mysql username, password, db name, state name searched
'''


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE '{}' ORDER BY id ASC""".format(argv[4]))
    for x in cur.fetchall():
        print(x)
    cur.close()
    db.close()
