#!/usr/bin/python3

""" A script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys


def list_states(user, password, database):
    """ Fuction that connects prints the  states in a database"""
    host = 'localhost'
    port = 3306

    try:
        # Connect to MySQL Server
        connection = MySQLdb.connect(host=host, port=port, user=user,
                                     passwd=password, database=database)

        # Create Cursor object to execute SQL query
        cursor = connection.cursor()

        # Execute query to select all states, ordered by state.id
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print the list of states
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL error:", e)

    finally:
        # close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


if __name__ == "__main__":
    # Check if all three argument are provided
    if (len(sys.argv) != 4):
        print("Usage: python script.py <username> <password> <database>")
    else:
        # Get command-line argument
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        list_states(user, password, database)
