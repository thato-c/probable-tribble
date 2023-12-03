import pymssql

# Establish a connection
connection = pymssql.connect(server='localhost',
                            user='testuser123',
                            password='testuser123',
                            database='License')

# Create a cursor from the connection
cursor = connection.cursor()

# Create Queries
getUsers = "SELECT * FROM Users"
createTable = ''' CREATE TABLE NEO (
                Neo_Id INT PRIMARY KEY,
                NeoRef_Id INT,
                Name varchar(100),
                AbsMagnitude int
                )
'''
# Execute SQL
cursor.execute(createTable)
#rows = cursor.fetchall()
connection.commit()

# Do something with the retrieved data
#print(rows)

# Close the cursor and conneciton
cursor.close()
connection.close()