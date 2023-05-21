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
    select_query = "SELECT name FROM students WHERE std_id = %s "
    value = (69,)
    cursor.execute(select_query, value)

    # Fetch the result
    results = cursor.fetchall()

    # Process and use the fetched data
    # Using for loop
    for data in results:
        print(data)

except mysql.connector.Error as error:
    print("ERROR: ", error)

