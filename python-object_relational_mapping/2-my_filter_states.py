#!/usr/bin/python3
"""Filter states based on user input"""

import MySQLdb
import sys


def filter_states_by_input():
    """Connects to the database and fetches states"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = db.cursor()

    sql_query = (
        "SELECT * FROM states WHERE name LIKE BINARY '{}' " 
        "ORDER BY id ASC"
    ).format(sys.argv[4])

    cursor.execute(sql_query)

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_input()
