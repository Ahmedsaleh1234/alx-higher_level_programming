#!/usr/bin/python3
"""script that lists all cities from the database"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    ch = con.cursor()
    ch.execute("select cities.id, cities.name, states.name  from cities\
               inner join states on cities.state_id = states.id")
    rows = ch.fetchall()
    for i in rows:
        print(i)
    ch.close()
    con.close()
