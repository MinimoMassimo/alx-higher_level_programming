#!/usr/bin/python3
'''
list all State objects that contain letter 'a'
command-line args: username, password, db
'''


from sys import argv
from model_state import Base, State
from sqlalchemy import select
from sqlalchemy import create_engine

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    stmt = select(State).where(State.name.like('%a%')).order_by(State.id)

    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print('{}: {}'.format(row[0], row[1]))
