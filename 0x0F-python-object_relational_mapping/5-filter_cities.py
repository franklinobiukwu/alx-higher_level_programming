#!/usr/bin/python3

"""
Write a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa

REQUIREMENTS
    - Your script should take 4 arguments: mysql username, mysql password,
      database name and state name (SQL injection free!)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server
      running on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - You can use only execute() once
    - The results must be displayed as they are in the example below
    - Your code should not be executed when imported
"""

import MySQLdb
import sys


def list_cities_in_state(username, password, database, state):
    host = 'localhost'
    port = 3306

    # Establish connection to database
    connection = MySQLdb.connect(user=username, passwd=password,
                                 host=host, database=database,  port=port)

    # Create cursor object
    with connection.cursor() as cursor:

        # Construct query
        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id
        """

        # Execute query
        cursor.execute(query, (state,))

        # Fetch selection
        cities = cursor.fetchall()

        if cities is not None:
            print(", ".join([city[0] for city in cities]))


if __name__ == '__main__':
    username, password, database, state = sys.argv[1:5]
    list_cities_in_state(username, password, database, state)
