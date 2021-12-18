#!/usr/bin/python3
""" Script that lists all cities by state from the database hbtn_0e_4_usa
"""


# Avoids excecution when imported
if __name__ == "__main__":

    # Uses MySQLdb methods to communicate with the database
    import MySQLdb
    # Makes able to take arguments from command line
    import sys

    argv = sys.argv
    # Open database connection
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         password=argv[2], database=argv[3])
    # Creates cursor object to perform SQL operations
    cursor = db.cursor()
    # Run SQL query
    cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM cities\
                   LEFT JOIN states \
                   ON cities.state_id = states.id\
                   ORDER BY cities.id ASC")
    # Extract/read query result
    result = cursor.fetchall()
    for rows in result:
        print(rows)
    # Close open connections
    cursor.close()
    db.close()
