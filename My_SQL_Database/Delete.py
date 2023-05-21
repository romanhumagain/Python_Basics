import mysql.connector

try:
    # Establish connection with mysql
    connection = mysql.connector.connect(
        host="localhost",
        password="",
        user="root",
        database = "new_db"
    )
    # Create a cursor object
    cursor = connection.cursor()

    # SQL query to select data from table
    select_query = "DELETE FROM students WHERE std_id = %s "
    value = (79,)

    # To execute query
    cursor.execute(select_query, value)

    #  To commit the changes
    connection.commit()
    print("Successfully Deleted !")


except mysql.connector.Error as error:
    print("ERROR: ", error)

finally:
    # To close the cursor and connection
    cursor.close()
    connection.close()


