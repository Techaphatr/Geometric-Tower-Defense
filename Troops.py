from EntityHandler import EntityHandler
import time
import math
import pygame

class Troops:
    def __init__(self, pos : tuple, stage : int = 0, typ : str = ""):
       self.x = pos[0]
       self.y = pos[1]
       self.value = False
       self.current_stage = stage
       self.type = typ
       self.last_attack = time.time()
       data = EntityHandler.TROOP_TYPE[typ]
       self.damage = data["damage"] + 3 * stage
       self.range = data["range"] + 5 * stage
       self.cooldown = data["cd"] - stage/18
       self.variance = pygame.image.load(f"Picture/Troops/{typ}/{self.__clamp(stage, 0, 10)}.png")
       self.isbuy = False

    def upgrade(self):
        self.current_stage += 1
        data = EntityHandler.TROOP_TYPE[self.type]
        self.damage = data["damage"] + 3 * self.current_stage
        self.range = data["range"] + 5 * self.current_stage
        self.cooldown = data["cd"] - self.current_stage/18
        self.variance = pygame.image.load(f"Picture/Troops/{self.type}/{self.__clamp(self.current_stage, 0, 10)}.png")

    def __clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))

    @property
    def position(self) -> tuple:
        return self.x, self.y