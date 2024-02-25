# an item that can be equipped and grants abilities when equipped
from skill import Skill


class Equippable:
    def __init__(self, name=""):
        self.name = name
        self.slot = ""
        self.price = 0
        self.skills = []
        self.set_stats()

    def __str__(self):
        output = self.name + "\n"
        output += self.slot + ", " + str(self.price) + "$\nSkills:\n"
        for i in range(len(self.skills)):
            output += str(self.skills[i]) + "\n"
        return output

    def get_skills(self):
        return self.skills

    def set_stats(self):
        try:
            with open('equipment.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if parts[0] == self.name:
                        self.price = int(parts[1])
                        self.slot = parts[2]
                        # remove the first three elements to just work with the skills (if they exist)
                        parts = parts[3:]
                        for i in range(len(parts)):
                            self.skills.append(Skill(parts[i]))

        except FileNotFoundError:
            print("Error: File 'equipment.txt' not found.")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return
