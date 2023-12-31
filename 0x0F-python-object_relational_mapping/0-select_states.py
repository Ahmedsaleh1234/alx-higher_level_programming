#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    con = MySQLdb.connect(host="localhost", port=3306,
                          user=argv[1], passwd=argv[2], db=argv[3])
    chan = con.cursor()
    chan.execute("select * from states")
    rows = chan.fetchall()
    for i in rows:
        print(i)

    chan.close()
    con.close()
