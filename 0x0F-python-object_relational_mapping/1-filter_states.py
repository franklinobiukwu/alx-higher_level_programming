#!/usr/bin/python3
""" Module that contains function that lists all states
with a name starting with N (upper N) from the database hbtn_0e_0_usa """

import MySQLdb
import sys


def list_states(username, password, database):
    """ A script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa """

    host = 'localhost'
    port = 3306

    try:
        # Establish connection with MySQL server
        connection = MySQLdb.connect(host=host, port=port, user=user,
                                     passwd=password, database=database)
        # Create cursor object
        cursor = connection.cursor()

        # Select all states with name starting with uppercase N
        cursor.execute("SELECT * FROM states WHERE name\
                            LIKE BINARY 'N%' ORDER BY id ASC")

        # Fetch all selected data
        rows = cursor.fetchall()

        # Print rows of fetched data
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"SQL error: {e}")

    finally:
        # Close cusor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


if __name__ == '__main__':
    if (len(sys.argv) != 4):
        print("Usage: python script.py <username> <password> <database name>")
    else:
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        list_states(user, password, database)
