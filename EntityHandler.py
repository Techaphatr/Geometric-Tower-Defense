import math

class EntityHandler():
    TROOP_LIST = []
    MONSTER_LIST = []
    TROOP_TYPE = [
        {"damage": 2, "range": 10},
    ]

    def __init__(self):
        pass

    def fire(self, troop, vfx = None):
        if len(EntityHandler.MONSTER_LIST) != 0:
            for monster in EntityHandler.MONSTER_LIST:
                distance = math.sqrt((monster.x - troop.x)**2 + (monster.y - troop.y)**2)
                if distance <= range:
                    monster.health -= troop.damage
                    if monster.health <= 0:
                        monster.died()

    def appearance(self, typ, key):
        pass

    def ability(self):
        pass