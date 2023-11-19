#!/usr/bin/python3
"""Script that takes in an argument and displays all values"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # Create a cursor object
    cur = db.cursor()
    # Prepare a parameterized query
    query = "SELECT * FROM states WHERE name = %s"
    # Execute the query with the user input as the parameter
    cur.execute(query, (sys.argv[4],))
    # Fetch all the results
    rows = cur.fetchall()
    # Print each row
    for row in rows:
        print(row)
    # Close the cursor
    cur.close()
    # Close the database connection
    db.close()
