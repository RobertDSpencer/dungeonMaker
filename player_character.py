# a player controlled unit that can traverse the dungeon and battle with enemies
class PlayerCharacter:
    def __init__(self, name: str, room: int, floor: int):
        self.name = name
        self.room = room
        self.floor = floor

    def move_rooms(self, new_room):
        self.room = new_room

    def move_floors(self, new_room, new_floor):
        self.room = new_room
        self.floor = new_floor

