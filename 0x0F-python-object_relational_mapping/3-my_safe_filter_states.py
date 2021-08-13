#!/usr/bin/python3
""" Script that takes arguments and displays
all values in the states table
where name matches the argument.
But this time, write one that is safe from MySQL injections! """
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
    i.execute("SELECT * FROM states \
               WHERE name=%s \
               ORDER BY states.id ASC", (sys.argv[4],))
    for row in i.fetchall():
        print(row)
    i.close()
    mysql_c.close()
