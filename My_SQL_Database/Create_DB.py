import mysql .connector

try:
    #Establish a connection to mysql server
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ""
    )
    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()
    # Query to create a new database
    create_db_query = "CREATE DATABASE new_db"

    # to execute query
    cursor.execute(create_db_query)
    print("Database Successfully Created")

except mysql.connector.Error as error:
    print("ERROR Occured: ", error)

finally:
    cursor.close()
    connection.close()



