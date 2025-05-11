import csv
import math


class database(super):

    __instance = None

    def __new__(cls):
        if database.__instance == None:
            database.__instance = super().__new__(cls)
        return database.__instance

    def __init__(self):
        self.__static_path = "data_holder\playerStatic.csv"
        self.config = {
            "Screen_Size": (1080, 720),
            "Defualt_Img": "Picture/MenuBG.png",
            "Hover_Img": ("Picture/bg1.png","Picture/bg2.png","Picture/bg3.png"),
            "Ingame_Img": "Picture/MainBG.png",
        }

    @staticmethod
    def distance(pos1: tuple, pos2 : tuple):
        return math.sqrt((pos2[1]-pos1[1])**2 + (pos2[0]-pos1[0])**2)

    def save(self, title, value):
        rows = []
        with open(self.__static_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows.append(headers)
            col_index = headers.index(title)
            for row in reader:
                rows.append(row)

        if len(rows) == 1:
            new_row = [""] * len(headers)
            new_row[col_index] = value
            rows.append(new_row)
        else:
            rows.append([""] * len(headers))
            rows[-1][col_index] = value

        with open(self.__static_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)