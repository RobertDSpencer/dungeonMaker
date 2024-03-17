import view_floor
from player_character import PlayerCharacter
from DungeonObj import Dungeon

input_commands = ["up", "down", "quit", "map"]


def check_user_input(user_input: str):
    if user_input.lower() in input_commands:
        return 1
    else:
        try:
            int(user_input)
            return 2
        except ValueError:
            return 0


def explore_dungeon(exp_player: PlayerCharacter, exp_dungeon: Dungeon):
    print("After a long journey, " + exp_player.name + " arrives at the dungeon of " + exp_dungeon.name + "! Delve "
                                                                                                          "boldly!")
    while True:
        dungeon_floors = exp_dungeon.floors  # all the floors of the dungeon. A list.
        current_floor = exp_player.floor  # the floor the player is currently on. An int
        current_room = exp_player.room  # the room the player is currently in
        current_passages = exp_dungeon.floors[current_floor].passage_array[current_room]  # all the connections to other
        # rooms. A list
        stair_up = False
        stair_down = False
        current_stairs = None
        if exp_player.floor == 0 and exp_player.room == 0:
            print(exp_player.name + " is at the entrance to the dungeon")
        else:
            print("You are on floor " + str(exp_player.floor) + " in room #" + str(exp_player.room))
        if dungeon_floors[current_floor].rooms > 1:
            print("Passages go to:")
            for i in range(len(current_passages)):
                if current_passages[i] == 1:
                    print("Room #" + str(i))
        for i in range(len(exp_dungeon.stairs)):
            if exp_dungeon.stairs[i].get_from() == [current_floor, current_room]:
                print("There is a staircase leading down here.")
                stair_down = True
                current_stairs = exp_dungeon.stairs[i]
            elif exp_dungeon.stairs[i].get_to() == [current_floor, current_room]:
                print("There is a staircase leading up here.")
                stair_up = True
                current_stairs = exp_dungeon.stairs[i]

        user_input = input("Enter a # to go to that room, up to go up, or down to go down")
        user_input = user_input.lower()
        input_result = check_user_input(user_input)
        if input_result == 0:
            print("Invalid command. Please enter a #, up or down")
        elif input_result == 1:  # This means a command was used. There should be one for every command here.
            if user_input == "up":
                if stair_up:
                    print("You go up the stairs.")
                    goto = current_stairs.get_from()
                    exp_player.floor = goto[0]
                    exp_player.room = goto[1]
                else:
                    print("There is no staircase leading up.")
            elif user_input == "down":
                if stair_down:
                    print("You go down the stairs.")
                    goto = current_stairs.get_to()
                    exp_player.floor = goto[0]
                    exp_player.room = goto[1]
                else:
                    print("There is no staircase leading down.")
            elif user_input == "map":
                print("You check your trusty map. (close it to continue)")
                floor_map = view_floor.graph_from_matrix(exp_dungeon.floors[current_floor].passage_array)
                view_floor.display_graph(floor_map)
            elif user_input == "quit":
                print("Goodbye!")
                break
            else:
                print("You don't know how to do that here.")
        elif input_result == 2:  # a number was input to go to another room
            user_input = int(user_input)
            if user_input == exp_player.room:
                print("You're already here.")
            elif user_input >= len(current_passages):
                print("There is no passage to room #" + str(user_input) + " here.")
            elif current_passages[user_input] == 1:
                print("You go to room " + str(user_input))
                exp_player.room = user_input
            elif current_passages[user_input] == 0:
                print("There is no passage to room #" + str(user_input) + " here.")
        print("\n")


if __name__ == '__main__':
    hiking_dungeon = Dungeon("Short Hike", 5, 10)
    player = PlayerCharacter("Lucas", 0, 0)
    explore_dungeon(player, hiking_dungeon)
