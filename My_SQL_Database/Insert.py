import mysql.connector

try:
    #Establishing a connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="new_db"
    )
    # creating cursor object to execute the SQL queries
    cursor = connection.cursor()

    # Inserting into table
    sql_queries = """
    INSERT INTO students(std_id, name, address, grade)
    VALUES(%s, %s, %s, %s)
    """
    values =(79, "Aswin", "Banepa", "A+" )
    cursor.execute(sql_queries, values)

    # commit the changes
    connection.commit()

    print("Successfully Inserted Data")

except mysql.connector.Error as error:
    print("ERROR: ", str(error))

# Closing the cursor and connection
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
