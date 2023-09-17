#!/usr/bin/python3
import sys
import MySQLdb

# Connect to the MySQL server
db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()

# Execute the SQL query to fetch all states
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the rows from the query result
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the database connection
db.close()
    # Execute the SQL query to fetch all states
cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the query result
rows = cursor.fetchall()

    # Print the results
for row in rows:
        print(row)

    # Close the database connection
db.close()

# Example usage
if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)