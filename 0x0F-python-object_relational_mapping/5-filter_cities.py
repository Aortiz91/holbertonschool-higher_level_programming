#!/usr/bin/python3
""" Script that  takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa
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
    cursor.execute("SELECT cities.name\
                   FROM cities\
                   LEFT JOIN states\
                   ON cities.state_id = states.id\
                   WHERE states.name = %(sname)s\
                   ORDER BY cities.id ASC",
                   {'sname': argv[4]})
    # Extract/read query result
    result = cursor.fetchall()
    rcities = ''
    for rows in range(len(result)):
        for columns in range(len(result[rows])):
            rcities = rcities + result[rows][columns] + ', '
    print("{}".format(rcities[:-2]))
    # Close open connections
    cursor.close()
    db.close()
