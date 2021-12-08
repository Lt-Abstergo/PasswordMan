import sqlite3
import sys
import traceback


def create_table(dbname):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS id(
                            name TEXT,
                            url TEXT,
                            username TEXT,
                            password TEXT,
                            entry_date TEXT
                            );""")
        print_file("database successfully created")
    except sqlite3.Error as error:
        print_file(error_handler(error))
    finally:
        conn.commit()
        conn.close()


def add_one(dbname, name, url, username, password, curr_time):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO id VALUES (?,?,?,?,?);", (name, url, username, password, curr_time))

    except sqlite3.Error as error:
        print_file(error_handler(error))

    finally:
        conn.commit()
        conn.close()


def add_multiple(dbname, item_list):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO id VALUES (?,?,?,?);", item_list)

    except sqlite3.Error as error:
        print_file(error_handler(error))

    finally:
        conn.commit()
        conn.close()


def show_all(dbname):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, * FROM id;")
        print_tb(cursor.fetchall())
    except sqlite3.Error as error:
        print_file(error_handler(error))

    finally:
        conn.commit()
        conn.close()


def delete_one(dbname, rowid):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM id where rowid=(?);", str(rowid))
    except sqlite3.Error as error:
        print_file(error_handler(error))

    finally:
        conn.commit()
        conn.close()


def delete_all(dbname):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM id ;")
        print_file("Removed all entries.")
    except sqlite3.Error as error:
        print_file(error_handler(error))

    finally:
        conn.commit()
        conn.close()


def get_row_id(dbname, name, url, username, password) -> list:
    row_id = []

    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT ROWID, * FROM id WHERE name=(?);", (name,))
        items = cursor.fetchall()
        print_tb(cursor.fetchall())

        for item in items:
            if item[2] == url and item[3] == username and item[4] == password:
                row_id.append(item[0])
        print_tb(cursor.fetchall())

    except sqlite3.Error as error:
        print_file(error_handler(error))

    finally:
        conn.commit()
        conn.close()
        return row_id


def table_exists(dbname) -> bool:
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", ("id",))
        items = cursor.fetchone()
        if items.__contains__('id'):
            return True
        else:
            return False
    except sqlite3.Error as error:
        print_file(error_handler(error))

    finally:
        conn.commit()
        conn.close()


def print_file(str_input):
    print(str_input)


def print_tb(items):
    for item in items:
        print(item)


def error_handler(error):
    exc_type, exc_value, exc_tb = sys.exc_info()
    er_string = "SQLite error: " + str(error)
    er_string += "\nSQLite traceback: "
    er_list = traceback.format_exception(exc_type, exc_value, exc_tb)
    for i in er_list:
        er_string += i
    return er_string
