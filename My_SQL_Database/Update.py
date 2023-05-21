import mysql.connector

try:
    # Establishing a connection with database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="new_db"
    )
    # Creating Object of cursor
    cursor = connection.cursor()
    # update syntax for MySQL
    update_query ="UPDATE students SET name = %s WHERE std_id = %s"
    values = ("Roman Humagain",69)

    # to exectue query
    cursor.execute(update_query, values)

    # To save the changes
    connection.commit()

    print("Successfully Updated :)")
except mysql.connector.Error as error:
    print("ERROR: ", error)

# Closing the cursor and connection
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
