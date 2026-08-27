import sqlite3

def create_table():

    conn = sqlite3.connect("customer.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers(
        id INTEGER PRIMARY KEY,
        phone_number TEXT NOT NULL,
        name TEXT NOT NULL,
        passward TEXT NOT NULL
        )
    """)

    conn.commit
    conn.close()

#Provide connection

def get_db():
    conn = sqlite3.connect("customer.db")

    try:
        yield conn

    finally:
        conn.close()