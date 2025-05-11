from EntityHandler import EntityHandler
import pygame
import random

class Monsters:
    def __init__(self, pos:tuple, stage:int = 0, path : list = []):
       EntityHandler.MONSTER_LIST.append(self)
       self.x = pos[0]
       self.y = pos[1]
       self.current_stage = stage
       self.current_speed = 1 + (1 * stage) + random.uniform(0,2)
       self.health = 10 + random.randint(3,5) * stage
       self.variance = pygame.image.load(f"Picture/Enemy/{stage}.png")
       self.path = path
       self.nearest_position = None

    def died(self):
        EntityHandler.MONSTER_LIST.remove(self)

    @property
    def position(self) -> tuple:
        return self.x, self.y