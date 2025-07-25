#!/usr/bin/python3
"""
Lists all states where name matches the argument from the database
hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()
    query = (
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
        .format(state_name)
    )
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
