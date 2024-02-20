# encompasses the whole dungeon; floors, monsters, traps, hazards and loot
from floor import Floor
class Dungeon:
    def __init__(self, name, depth, level):
        self.name = name
        self.depth = depth
        self.level = level
        self.floors = []
        for i in range(self.depth):
            self.new_floor()  # generates a new floor for the dungeon

    def new_floor(self):  # TODO flesh out floor creation
        self.floors.append(Floor())


