from EntityHandler import EntityHandler

class Troops:
    def __init__(self, pos : tuple, stage : int = 0):
       self.x = pos[0]
       self.y = pos[1]
       self.current_stage = stage
       data = EntityHandler.TROOP_TYPE[stage]
       self.damage = data.damage
       self.range = data.range

    @property
    def position(self) -> tuple:
        return self.x, self.y