#!/usr/bin/python3
'''
prints the first state object
command-line args: mysql username, password, name
'''


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import select

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    stmt = select(State).where(State.id == 1)
    with engine.connect() as conn:
        rows = conn.execute(stmt)
        if len(rows) == 0:
            print('Nothing')
            return
        for x in rows:
            print("{}: {}".format(x[0], x[1]))
