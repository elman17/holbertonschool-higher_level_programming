#!/usr/bin/python3
"""SQL injection"""

import MySQLdb
import sys


def filter_states_safely():
    """Connects to the database and fetches states safely"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = db.cursor()

    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(sql_query, (sys.argv[4],))

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states_safely()
