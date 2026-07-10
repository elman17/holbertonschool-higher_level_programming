#!/usr/bin/python3
"""Cities by states"""

import MySQLdb
import sys


def list_cities_by_state():
    """Connects to the database and fetches cities with their state names."""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = db.cursor()

    sql_query = (
        "SELECT cities.id, cities.name, state.name "
        "FROM cities "
        "JOIN states ON cities.state_id = state.id "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(sql_query)
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_by_state()
