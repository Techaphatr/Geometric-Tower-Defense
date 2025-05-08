import csv
import os


class database(super):

    __instance = None

    def __new__(cls):
        if database.__instance == None:
            database.__instance = super().__new__(cls)
        return database.__instance

    def __init__(self):
        self.__data_path = "data_holder\playerdata.csv"
        self.__static_path = "data_holder\playerStatic.csv"
        self.config = {
            "Screen_Size": (1080, 720),
        }

    def load_player_data(self, username) -> list:
        with open(self.__data_path, mode="r", newline="", encoding='utf-8') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == username:
                    return row

    def save_player_data(self, username):
        rows = []
        with open(self.__data_path, mode="r", newline="", encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows.append(headers)

            for row in reader:
                if row[0] == username:
                    pass
                    # What to save
                rows.append(row)

        with open(self.__data_path, mode="w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    
    def save(self, title, value):
        pass