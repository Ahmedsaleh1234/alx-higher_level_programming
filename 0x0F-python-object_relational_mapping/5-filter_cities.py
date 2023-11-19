#!/usr/bin/python3
"""All cities by state"""
import MySQLdb
from sys import argv
con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                      passwd=argv[2], db=argv[3])
ch = con.cursor()
ch.execute("select cities.name from cities\
           inner join states on cities.state_id = states.id\
           where states.name = %s", [argv[4]])
rows = ch.fetchall()
j = []
for i in rows:
    j.append(i[0])
print(", ".join(j))
ch.close()
con.close()
