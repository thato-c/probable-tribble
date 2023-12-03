import pymssql

# Establish a connection
connection = pymssql.connect(server='localhost',
                            user='testuser123',
                            password='testuser123',
                            database='License')

# Create a cursor from the connection
cursor = connection.cursor()

# Execute SQL
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()

# Do something with the retrieved data
print(rows)

# Close the cursor and conneciton
cursor.close()
connection.close()