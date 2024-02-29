# a "species" of entity that must be pacified or killed to progress.
from equippable import Equippable
from skill import Skill
import random


class Mob:
    def __init__(self, name="vapor", level=0, constitution=0, block=0, evade=0, reduce=0, strength=0, will=0,
                 dexterity=0, skill=0, negotiation=0, charisma=0, hostility=0, body_type="AMORPHOUS"):
        self.name = name
        self.hostility = hostility
        self.charisma = charisma
        self.negotiation = negotiation
        self.skill = skill
        self.dexterity = dexterity
        self.will = will
        self.strength = strength
        self.reduce = reduce
        self.evade = evade
        self.block = block
        self.level = level
        self.constitution = constitution
        self.body_type = body_type
        self.speed = 0
        self.skills = []
        self.set_stats(self.name)
        if self.body_type == "HUMANOID":
            self.slots = [["weapon"], ["off hand"], ["body"], ["legs"], ["head"]]
        elif self.body_type == "MONOPOD":
            self.slots = [["Shoe"]]
        elif self.body_type == "AMORPHOUS":
            self.slots = []
        else:
            self.slots = []
        self.set_equipment()
        self.set_skills()

    def __str__(self):
        output = self.name + "\n"
        output += "LV: " + str(self.level) + " TYP: " + self.body_type + "\n"
        output += "CON: " + str(self.constitution) + " BLK: " + str(self.block) + "\n"
        output += "EVD: " + str(self.evade) + " RED: " + str(self.reduce) + "\n"
        output += "STR: " + str(self.strength) + " WIL: " + str(self.will) + "\n"
        output += "DEX: " + str(self.dexterity) + " SKL: " + str(self.skill) + "\n"
        output += "CHA: " + str(self.charisma) + " NEG: " + str(self.negotiation) + "\n"
        output += "HOS: " + str(self.hostility) + " SPD: " + str(self.speed) + "\n"
        for i in range(len(self.skills)):
            specefic_skill = self.skills[i]
            output += specefic_skill.get_name()
            output += "\n"
        return output

    def set_stats(self, name):  # sets the mob stats to a value stored in data.
        try:
            with open('monster_stats.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if parts[0] == name:
                        self.name = parts[0]
                        self.level = int(parts[1])
                        self.constitution = int(parts[2])
                        self.block = int(parts[3])
                        self.evade = int(parts[4])
                        self.reduce = int(parts[5])
                        self.strength = int(parts[6])
                        self.will = int(parts[7])
                        self.dexterity = int(parts[8])
                        self.skill = int(parts[9])
                        self.negotiation = int(parts[10])
                        self.charisma = int(parts[11])
                        self.hostility = int(parts[12])
                        self.speed = int(parts[13])
                        self.body_type = parts[14]
                        return
                print(f"Monster '{name}' not found.")
                return
        except FileNotFoundError:
            print("Error: File 'monster_stats.txt' not found.")
            return
        except Exception as e:
            print(f"An error occurred in set_stats: {e}")
            return

    def set_skills(self):
        self.skills.append(Skill("push"))
        try:  # add the monster's innate skills
            with open('monster_skills.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if parts[0] == self.name:
                        for i in range(len(parts) - 1):
                            self.skills.append(Skill(parts[i + 1]))
            file.close()
        except FileNotFoundError:
            print("Error: File 'monster_skills.txt' not found.")
            return
        except Exception as e:
            print(f"An error occurred in set_skills: {e}")
            return
        for i in range(len(self.slots)):
            # extract the skills from the equipment
            equipment_skills = self.slots[i][1].get_skills()
            for j in range(len(equipment_skills)):
                self.skills.append(equipment_skills[j])

    def set_equipment(self):
        try:
            with open('monster_equipment.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if parts[0] == self.name:
                        equip_slots = len(self.slots)  # the number of equip slots for the body type
                        j = 0  # j keeps track of which part of the line we are on. it only increments
                        for i in range(equip_slots):  # for each equipment slot...
                            possibilities = []  # all possible equipment
                            percent_tally = 0
                            while True:  # while we don't see a semicolon
                                j += 1

                                # tallies up the percentages of the possible items;
                                # this is so "no item" can have the proper percentage.
                                if parts[j] != ";":
                                    possibilities.append([parts[j], int(parts[j + 1])])
                                    percent_tally += int(parts[j + 1])
                                    j += 1
                                else:
                                    break  # semicolon is the break char. It means no more items are possible
                            # now, to add the "nothing" option
                            nothing_percent = 100 - percent_tally
                            if nothing_percent < 0:
                                nothing_percent = 0
                            possibilities.append(["", nothing_percent])
                            die_roll = random.randint(1, 100)
                            percentage_stack = 0  # "stacks" the percentages up. Once the stack exceeds or equals the
                            # roll, the item is selected.
                            k = 0
                            while True:
                                percentage_stack += possibilities[k][1]
                                if die_roll <= percentage_stack:
                                    self.slots[i].append(Equippable(possibilities[k][0]))
                                    break
                                else:
                                    k += 1

        except FileNotFoundError:
            print("Error: File 'monster_equipment.txt' not found.")
            return
        except Exception as e:
            print(f"An error occurred in set_equipment: {e}")
            return


def test():
    test_goblin = Mob("GoblinLV1")
    print(test_goblin)


test()
