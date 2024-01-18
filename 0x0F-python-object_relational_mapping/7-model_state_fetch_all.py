#!/usr/bin/python3

"""
    Write a script that lists all State objects from the database hbtn_0e_6_usa

        REQUIREMENTS
        - Your script should take 3 arguments: mysql username,
          mysql password and database name
        - You must use the module SQLAlchemy
        - You must import State and Base from model_state -
          from model_state import Base, State
        - Your script should connect to a MySQL
          server running on localhost at port 3306
        - Results must be sorted in ascending order by states.id
        - The results must be displayed as they are in the example below
        - Your code should not be executed when imported
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states(username, password, database):
    """
        Function that lists all state objects from a database
    """

    host = 'localhost'
    port = 3306

    con_str = f"mysql+mysqldb://{username}:{password}@{host}:{port}/{database}"

    engine = create_engine(con_str, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id).all()

    if states:
        for state in states:
            print(f"{state.id}: {state.name}")

    session.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: script.py <database username> \
<database password> <database name>")
    else:
        username, password, database = sys.argv[1:4]
        list_states(username, password, database)
