import mysql.connector

try:
    # Establish a connection with database
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "new_db"
    )
    # creating cursor object to execute SQL queries
    cursor = connection.cursor()

    # creating a table
    create_table_quries = """
    CREATE TABLE IF NOT EXISTS students(
    std_id INT PRIMARY KEY AUTO_INCREMENT,
    name varchar(40),
    address varchar(40),
    grade varchar(10)
    )
    """
    cursor.execute(create_table_quries)
    # commit the changes
    connection.commit()

    #close the cursor and connection
    cursor.close()
    connection.close()
    print("Table successfully created")

except mysql.connector.Error as error:
    print("ERROR Occured: ", error)

finally:
    # close the cursor and connection even if there is error
    cursor.close()
    connection.close()