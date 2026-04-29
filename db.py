import sqlite3

DB_NAME = "Messages.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Users
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT,
               password TEXT,
               role TEXT)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Messages
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT,
               role TEXT,
               message TEXT,
               timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)""")

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


conn.commit()
conn.close()