#!/usr/bin/python3

"""
    Write a script that lists all cities from the database hbtn_0e_4_usa

    REQUIREMENTS
    - Your script should take 3 arguments:
        mysql username, mysql password and database name
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL
      server running on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - You can use only execute() once
    - Results must be displayed as they are in the example below
    - Your code should not be executed when imported
"""

import MySQLdb
import sys


def list_cities(username, password, database):
    host = 'localhost'
    port = 3306

    # Connect to database
    connection = MySQLdb.connect(user=username, passwd=password,
                                 host=host, database=database, port=port)

    # Create cursor object
    cursor = connection.cursor()

    # Query to select all cities
    query = "SELECT cities.name AS cities_name, states.name AS state_name\
            FROM cities\
            JOIN states ON cities.state_id=states.id"

    # Execute query
    cursor.execute(query)

    # Fetch all selected data
    cities = cursor.fetchall()

    # Print each selection
    for city in cities:
        print(city)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: script.py  <username> <password> <database name>")
    else:
        username, password, database = sys.argv[1:4]
        list_cities(username, password, database)
