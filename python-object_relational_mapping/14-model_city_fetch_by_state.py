#!/usr/bin/python3
"""Cities in states"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_cities_by_state():
    """Connects to the database and fetches cities joined with states"""
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(db_url ,pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id.asc())
        .all()
    )

    for city, state in results:
        print("{}: ({})".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    fetch_cities_by_state()
