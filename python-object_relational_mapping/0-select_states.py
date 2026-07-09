#!/usr/bin/python3
"""Get all states"""

import sys
import MySQLdb


db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

print("Connected!")