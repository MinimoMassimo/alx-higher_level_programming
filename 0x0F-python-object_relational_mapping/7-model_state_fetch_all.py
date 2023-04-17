#!/usr/bin/python3
'''
lists all State objects from db
command-line args: username, password, db name
'''


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    # create session: connect to engine
    Sess = sessionmaker(engine)
    sess = Sess()

    # execute the syntax
    for x in sess.query(State).order_by(State.id):
        print('{}: {}'.format(x.id, x.name))
