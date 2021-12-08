import csv
from datetime import datetime as time
from urllib.parse import urlparse as parse

import AES256Handler as encA
import DatabaseHandler as dbH


class BusinessHandler:
    __doc__ = """Handles Business logic for the object"""
    __public_key: str
    database_name: str

    def __init__(self, pkey):
        self.database_name = "pass_man.db"
        self.__public_key = pkey
        dbH.create_table(self.database_name)

    def __get_public_key(self) -> str:
        return self.__public_key

    #   needs to be initiated
    def set_public_key(self, p_key):
        self.__public_key == p_key

    #   Extracts backup data from the
    def extract_backup(self, backup_path):
        try:
            with open(backup_path, newline='')as csv_file:
                spam_reader = csv.reader(csv_file, delimiter=',')
                for row in spam_reader:
                    name, url, username, password = row
                    if name == "name" and url == "url" and username == "username" and password == "password":
                        pass
                    else:
                        self.add_new(url, username, password, name)
        except OSError as error:
            dbH.error_handler(error)
        finally:
            csv_file.close()
            print

    def encrypt_database(self):
        pass

    def save_to_disk(self, source):
        pass

    def add_new(self, url: str, username: str, password: str, name=None):
        if name is None:
            name_netloc = parse(url).netloc
            dbH.add_one(self.database_name, name_netloc, url, username, password, time.now())

        else:
            dbH.add_one(self.database_name, name, url, username, password, time.now())

    def reset_db(self):
        dbH.delete_all(self.database_name)

    def encrypt_data(self, data: str) -> str:
        cipher = encA.encrypt(data, self.__public_key)
