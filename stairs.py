# the stairs that allow traversal between one floor and another
class Staircase:
    def __init__(self, floor_from=0, floor_to=0, room_from=0, room_to=0):
        self.floor_from = floor_from
        self.room_from = room_from  # the room and floor of the end of the staircase that is closer to the entrance
        self.floor_to = floor_to
        self.room_to = room_to  # the room and floor of the end of the staircase that is further from the entrance

    def __str__(self):
        return ("from " + str(self.floor_from) + "-" + str(self.room_from) + " to " + str(self.floor_to) + "-"
                + str(self.room_to))

    def set_room_to(self, new_to):
        self.room_to = new_to

    def set_room_from(self, new_from):
        self.room_from = new_from

