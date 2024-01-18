#!/usr/bin/python3

"""
    Write a script that prints the first State object
    from the database hbtn_0e_6_usa

    REQUIREMENT
    - Your script should take 3 arguments:
        mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state -
      from model_state import Base, State
    - Your script should connect to a MySQL server running
      on localhost at port 3306
    - The state you display must be the first in states.id
    - You are not allowed to fetch all states from the
      database before displaying the result
    - The results must be displayed as they are in the example below
    - If the table states is empty, print Nothing followed by a new line
    - Your code should not be executed when imported
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_first_state(username, password, database):
    """
        Function that prints first state object
    """

    host = 'localhost'
    port = 3306

    conn_str = f"mysql+mysqldb://{username}:\
            {password}@{host}:{port}/{database}"

    engine = create_engine(conn_str)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    username, password, database = sys.argv[1:4]
    print_first_state(username, password, database)
