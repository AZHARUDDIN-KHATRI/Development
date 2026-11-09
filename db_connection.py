import mysql.connector

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_MYSQL_PASSWORD",
            database="medidb"
        )

        print("Database connected successfully!")
        return connection

    except mysql.connector.Error as error:
        print("Database error:", error)
        return None