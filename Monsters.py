from EntityHandler import EntityHandler

class Monsters:
    def __init__(self, pos:tuple, stage:int = 0, speed:int = 2, health:int = 10):
       EntityHandler.MONSTER_LIST.append(self)
       self.x = pos[0]
       self.y = pos[1]
       self.current_stage = stage
       self.current_speed = speed
       self.health = health

    def died(self):
        EntityHandler.MONSTER_LIST.remove(self)

    @property
    def position(self) -> tuple:
        return self.x, self.y