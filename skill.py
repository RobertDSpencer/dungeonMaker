# a skill that is either active or passive. it changes stats and/or launches an attack when activated.
from effect import Effect
from named_effect import NamedEffect

# these are the named effects; special effects that do something hard-coded instead of modifying a stat. Examples
# include status effects and calling for help
named_effects = ["Plague", "CallWildDog", "Incorporeal", "Nuisance", "Gag"]


def count_semicolons(parts):
    semicolon_count = 0
    for string in parts:
        if isinstance(string, str) and ';' in string:
            semicolon_count += 1
    return semicolon_count


class Skill:
    def __init__(self, name=""):
        self.name = name
        self.power = 0
        self.passive = False
        self.hit_range = 0
        self.effects = []
        # get the data from skills.txt
        self.set_data()

    def __str__(self):
        output = self.name + "\n"
        output += "PWR: " + str(self.power) + " RANGE: " + str(self.hit_range) + "\n"
        if self.passive:
            output += "PASSIVE\n"
        else:
            output += "ACTIVE\n"
        output += "Effects:\n"
        for i in self.effects:
            output += str(i) + "\n"
        if len(self.effects) == 0:
            output += "NO EFFECTS"
        return output

    def set_data(self):
        try:
            name = self.name
            with open('skills.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if parts[0] == self.name:
                        self.power = parts[1]
                        if parts[2] == "Y":
                            self.passive = True
                        elif parts[2] == "N":
                            self.passive = False
                        else:
                            print("ERROR!" + self.name + " has an incorrect passive value.")
                            return
                        self.hit_range = parts[3]
                        i = 0  # which effect are we on?
                        j = 4  # which part of parts are we on? Starts at 3
                        effect_num = count_semicolons(parts)  # the number of semicolons is the number of effects
                        while i < effect_num:
                            if parts[j] in named_effects:
                                self.effects.append(NamedEffect(parts[j], parts[j + 1]))
                                j += 3
                            else:
                                self.effects.append(Effect(parts[j], parts[j + 1], parts[j + 2], parts[j + 3]))
                                j += 4
                            i += 1
                        break
            file.close()
        except FileNotFoundError:
            print("Error: File 'skills.txt' not found.")
            return
        except Exception as e:
            print(f"An error occurred in skills: {e}")
            return

    def get_effects(self):
        return self.effects

    def get_name(self):
        return self.name


