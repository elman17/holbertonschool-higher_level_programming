#!/usr/bin/python3
"""All cities by state"""

import MySQLdb
import sys


def filter_cities_by_state():
    """Connects to the database and fetches citites for a specific state."""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = db.cursor()

    sql_query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(sql_query, (sys.argv[4],))
    query_rows = cursor.fetchall()

    cities_list = [row[0] for row in query_rows]

    print(", ".join(cities_list))

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities_by_state()
