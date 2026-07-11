#!/usr/bin/python3
"""Get a state"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state_by_name():
    """Connects to tha databse and find the state with its name"""
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    get_state_by_name()
