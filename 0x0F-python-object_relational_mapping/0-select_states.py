#!/usr/bin/python3
""" Script that lists all states from the database """
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
    i.execute("SELECT * FROM states ORDER BY states.id ASC;")
    for row in i.fetchall():
        print(row)
    i.close()
    mysql_c.close()
