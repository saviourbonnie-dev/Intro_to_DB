#!/usr/bin/python3
"""
Creates the database 'alx_book_store' in MySQL server.
If it already exists, script does not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Update credentials if needed
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # enter your MySQL root password if you set one
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
