# a single floor in the dungeon. Has a description, threats, loot, passages, rooms, and hidden elements
from stairs import Staircase

class Floor:
    def __init__(self, description="", rooms=0, depth=0, level=0, encounter_table=None, threat_table=None, passage_array=None,
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
        self.floor_traversal = floor_traversal  # an array of stair objects that take the party between floors.
        # Todos: (all these classes must be made before floor can begin):
        # TODO encounter obj.
        # TODO door trap obj.
        # TODO hazard obj.

    def new_floor_entrance(self, entrance=Staircase()):  # adds the floor's entrance point,
        # to move to the previous floor
        entrance.set_room_to(1)  # sets the endpoint of this floor's entrance to the first room
        self.floor_traversal.append(entrance)

    def new_floor_exit(self, egress=Staircase()):  # adds the floor's exit, to move to the next floor
        egress.set_room_from(self.rooms)  # sets the origin of this floor's exit to the last room.
        self.floor_traversal.append(egress)


