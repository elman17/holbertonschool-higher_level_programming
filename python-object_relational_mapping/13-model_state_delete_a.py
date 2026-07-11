#!/usr/bin/python3
"""Delete states"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states_by_a():
    """Connect to the database and delete a state"""
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .delete(synchronize_session="fetch")
    )

    session.commit()

    session.close()


if __name__ == "__main__":
    delete_states_by_a()
