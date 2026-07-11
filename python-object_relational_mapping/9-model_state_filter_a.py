#!/usr/bin/python3
"""Contain `a`"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def filter_states_by_a():
    """Connect to the database and fetches contain a states."""
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .order_by(State.id.asc())
        .all()
    )

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    filter_states_by_a()
