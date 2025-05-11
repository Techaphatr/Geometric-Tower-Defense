import math
import pygame

class EntityHandler():
    TROOP_LIST = []
    MONSTER_LIST = []
    TROOP_TYPE = {
        "Circle": {"damage": 3, "range": 70, "cd": 1},
        "Triangle": {"damage": 5, "range": 120, "cd": 1},
        "Square": {"damage": 7, "range": 70, "cd": 1},
    }

    @classmethod
    def check_merge(cls, x, y) -> tuple:
        for grid in cls.TROOP_LIST:
            if grid.x == x and grid.y == y:
                return True, grid
        return False, None

    @classmethod
    def check_win(cls) -> bool:
        return len(cls.MONSTER_LIST) == 0

    @classmethod
    def reset(cls):
        cls.TROOP_LIST = []
        cls.MONSTER_LIST = []

    @staticmethod
    def distance(pos1: tuple, pos2 : tuple):
        return math.sqrt((pos2[1]-pos1[1])**2 + (pos2[0]-pos1[0])**2)

    @classmethod
    def fire(cls, troop, typ):
        if len(cls.MONSTER_LIST) != 0:
            closest = None
            dis = troop.range + 1
            hit = 0
            for monster in cls.MONSTER_LIST:
                if cls.distance(monster.position, troop.position) < dis:
                    closest = monster
                    dis = cls.distance(monster.position, troop.position)
                if typ == "Circle":
                    distance = cls.distance(monster.position, troop.position)
                    if distance <= troop.range:
                        hit += 1
                        monster.health -= troop.damage
                        if monster.health <= 0:
                            monster.died()
            if closest == None:
                return False
            if typ == "Triangle":
                closest.health -= troop.damage
                hit += 1
                if closest.health <= 0:
                    closest.died()
            elif typ == "Square":
                closest.health -= troop.damage
                hit += 1
                if closest.health <= 0:
                    closest.died()
            elif hit == 0:
                return False
            return True
        else:
            return False
