#!/usr/bin/python3
"""that takes in an argument and displays all values"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    ch = con.cursor()
    ch.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])
    rows = ch.fetchall()
    for i in rows:
        print(i)
    ch.close()
    con.close()
