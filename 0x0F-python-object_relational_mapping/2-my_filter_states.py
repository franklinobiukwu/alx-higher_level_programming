#!/usr/bin/python3

"""
    A script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys


def display_states(username, password, database, searched):
    host = 'localhost'
    port = 3306

    try:
        # Establish connection with MySQL server
        connection = MySQLdb.connect(user=username, passwd=password,
                                     database=database, host=host, port=port)
        # Create cursor object
        cursor = connection.cursor()

        # Query to select searched term from state table
        query = """SELECT * FROM states WHERE name LIKE BINARY
        '{}' ORDER BY id ASC""".format(searched)

        # Execute query
        cursor.execute(query)

        # Fetch all selected data
        states = cursor.fetchall()

        # Print each state
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print(f"MySQL error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == '__main__':

    if len(sys.argv) != 5:
        print("Usage: python script.py <username>\
                <password> <database name> <search term>")
    else:
        username, password, database, searched = sys.argv[1:5]

        display_states(username, password, database, searched)
