import sqlite3

conn = sqlite3.connect("pass_man.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE id(
                    name TEXT,
                    url TEXT,
                    username TEXT,
                    password TEXT
                    )""")
print("database successfully created")
conn.commit()
conn.close()
