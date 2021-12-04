import sqlite3


def create_table(dbname):
    conn = sqlite3.connect(dbname + ".db")
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


def add_one(dbname, name, url, username, password):
    conn = sqlite3.connect(dbname + ".db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO id VALUES (?,?,?,?)", (name, url, username, password))
    conn.commit()
    conn.close()


def add_multiple(dbname, list):
    conn = sqlite3.connect(dbname + ".db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO id VALUES (?,?,?,?)", list)
    conn.commit()
    conn.close()


def show_all(dbname):
    conn = sqlite3.connect(dbname + ".db")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * from id")
    items = cursor.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()


def delete_one(rowid):
    conn = sqlite3.connect(dbname + ".db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM id where rowid=(?)", str(rowid))
    conn.commit()
    conn.close()


def get_row_id(dbname, )


dbname = "pass_man"
show_all(dbname)
delete_one(1)
show_all(dbname)
