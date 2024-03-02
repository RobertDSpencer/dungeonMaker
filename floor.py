# a single floor in the dungeon. Has a description, threats, loot, passages, rooms, and hidden elements
from stairs import Staircase
from door_trap import DoorTrap
import random
import networkx as nx
import view_floor


class Floor:
    def __init__(self, description="", rooms=0, depth=0, level=0, encounter_table=None, threat_table=None,
                 passage_array=None,
                 floor_traversal=None):
        if floor_traversal is None:
            floor_traversal = []
        if passage_array is None:
            passage_array = []
        if threat_table is None:
            threat_table = []
        if encounter_table is None:
            encounter_table = []

        self.description = description  # the description of the floor. Displayed in the string
        self.rooms = rooms  # the number of rooms in the dungeon floor
        self.depth = depth  # how far down this specefic floor is
        self.level = level  # the level of threat on the floor.
        self.encounter_table = encounter_table  # a list of encounters for each room, the enemies in each room.
        self.threat_table = threat_table  # the threats in the room. Both static hazards like lava, acid, pits. Also
        # the traps leading into the room, e.g. tripwires, pressure plates. Only the traps leading out of the room,
        # not in
        self.passage_array = passage_array  # the rooms are a graph, and the passage array is the edges
        # between vertices (rooms).
        self.passage_array_populate()
        self.generate_passages_first()
        self.floor_traversal = floor_traversal  # an array of stair objects that take the party between floors.

    def passage_array_populate(self):  # populates the passage array with 0s (no connection)
        passage_array = self.passage_array
        for i in range(self.rooms):
            self.passage_array.append([])
            for j in range(self.rooms):
                self.passage_array[i].append(0)

    def generate_passages_first(self):  # generates the minimum number of passages
        vertices = self.rooms
        min_passages = vertices - 1
        for i in range(min_passages):  # generates each mandatory passage
            valid_hall = False
            origin_point = 0
            end_point = 0
            while not valid_hall:
                origin_point = random.randint(0, self.rooms - 1)
                end_point = random.randint(0, self.rooms - 1)
                if origin_point != end_point and self.passage_array[origin_point][end_point] == 0:
                    valid_hall = True  # if the start and end are different, the hall is valid. The hall may not already
                    # exist either.
            self.passage_array[origin_point][end_point] = 1
            self.passage_array[end_point][origin_point] = 1  # the conection goes both ways, so two options are set to 1



    def new_floor_entrance(self, entrance=Staircase()):  # adds the floor's entrance point,
        # to move to the previous floor
        entrance.set_room_to(1)  # sets the endpoint of this floor's entrance to the first room
        self.floor_traversal.append(entrance)

    def new_floor_exit(self, egress: Staircase):  # adds the floor's exit, to move to the next floor
        egress.set_room_from(self.rooms)  # sets the origin of this floor's exit to the last room.
        self.floor_traversal.append(egress)


def test():
    test_floor = Floor("TestFloor", 6)
    graph = view_floor.graph_from_matrix(test_floor.passage_array)
    view_floor.display_graph(graph)


test()
