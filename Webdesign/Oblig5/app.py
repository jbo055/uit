import mysql.connector
from mysql.connector import Error

def connect_to_remote_mysql():
    connection = None
    try:
        # Connect to the remote MySQL server
        connection = mysql.connector.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'connectionacc',
            password = 'Juli1anette',
            database = 'arrangementshåndtering'
        )

        if connection.is_connected():
            print("Connected to the MySQL server")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            current_db = cursor.fetchone()
            print("You're connected to database: ", current_db)
            return connection
        
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    connect_to_remote_mysql()

