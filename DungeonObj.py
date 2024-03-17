# encompasses the whole dungeon; floors, monsters, traps, hazards and loot
from floor import Floor
from stairs import Staircase
import view_floor


class Dungeon:
    def __init__(self, name, depth, level, stairs="DEFAULT"):
        self.name = name
        self.depth = depth
        self.level = level
        self.floors = []
        self.stairs = self.stair_generation(stairs)
        for i in range(self.depth + 1):  # there is a floor 0 that is just the entrance.
            self.new_floor(i)  # generates a new floor for the dungeon at a depth of i
        self.endpoint = [self.floors[len(self.floors) - 1].rooms, self.depth]  # room, floor

    def __str__(self):
        output = ("This is the dungeon of " + str(self.name) + ". It boasts " + str(
            self.depth) + " floors, and a level of "
                  + str(self.level) + ". It has " + str(len(self.stairs)) + " staircases. They are as follows: ")
        for i in range(len(self.stairs)):
            output += "\n" + str(self.stairs[i])
        return output


    def new_floor(self, floor_num):  # TODO flesh out floor creation
        # the floor_num is which floor number this floor is. It also serves as the number of rooms -1
        # (e.g., floor 0 has 1 room, floor 10 has 11 rooms)
        new_floor = Floor("This floor #" + str(floor_num), floor_num + 1, floor_num, self.level)
        if floor_num > 0:  # the first floor (floor 0) has no entrance; it is the entrance.
            new_floor.new_floor_entrance(self.stairs[floor_num - 1])
        if floor_num < self.depth:  # the last floor does not have an exit, it is the end
            new_floor.new_floor_exit(self.stairs[floor_num])
        self.floors.append(new_floor)

    def stair_generation(self, directions):  # generates every staircase for the dungeon
        flight = []
        if directions == "DEFAULT":
            stair_num = self.depth  # the top and bottom floors only need one staircase,
            # the rest have two and share the staircase with the floor above and below
            for i in range(stair_num):
                flight.append(Staircase(i, i + 1))  # creates a staircase from the current floor to the next floor.
                # The default room values will be corrected in the floor.
        return flight


def test_dungeon():
    test = Dungeon("test", 5, 10)
    for i in range(len(test.floors)):
        graph = view_floor.graph_from_matrix(test.floors[i].passage_array)
        view_floor.display_graph(graph)
