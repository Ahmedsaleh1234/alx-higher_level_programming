#!/usr/bin/python3
"""lists all states with a name starting with N"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    ch = con.cursor()
    ch.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")
    rows = ch.fetchall()
    for i in rows:
        print(i)
    ch.close()
    con.close()
