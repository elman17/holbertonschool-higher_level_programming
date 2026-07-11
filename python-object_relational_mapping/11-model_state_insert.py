#!/usr/bin/python3
"""Add a new state"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def insert_new_state():
    """Connects to the database and inserts a new state"""
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)

    session.commit()

    print("{}".format(new_state.id))

    session.close()


if __name__ == "__main__":
    insert_new_state()
