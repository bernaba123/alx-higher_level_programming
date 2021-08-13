#!/usr/bin/python3
""" Script that takes in the name of a state as an argument
and lists all cities of that state, using the database """
import MySQLdb
import sys

if __name__ == '__main__':

    mysql_c = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        host="localhost",
        port=3306)

    i = mysql_c.cursor()
    i.execute("""SELECT cities.name
                 FROM cities INNER JOIN states
                 ON states.id=cities.state_id
                 WHERE states.name=%s""", (sys.argv[4],))
    rows = i.fetchall()
    arr = list(row[0] for row in rows)
    print(*arr, sep=", ")
    i.close()
    mysql_c.close()
