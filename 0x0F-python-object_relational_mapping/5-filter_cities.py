#!/usr/bin/python3
"""lists all cities filtered by state
from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="127.0.0.1", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT c.name FROM cities AS c inner join states
            AS s on c.state_id = s.id where s.name =%s
            order by c.id""", (sys.argv[4], ))
    rows = cur.fetchall()
    ltemp = [row[0] for row in rows]
    print(*ltemp, sep=", ")
    cur.close()
    db.close()
