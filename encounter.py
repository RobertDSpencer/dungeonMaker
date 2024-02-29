# a group of mobs, encountered together, in one room.
from mob import Mob
import random

# these are all the pools of possible mobs in an encounter
dilapidated_chapel = [Mob("GoblinLV1"), Mob("GoblinLV2"), Mob("SandMinion"), Mob("Staubgheist"), Mob("Monopod"),
                      Mob("GiantRat")]
mob_pools = [dilapidated_chapel]
pool_names = ["dilapidated_chapel"]

first_guard = [Mob("GoblinLV1")]
chapel_confrontation = [Mob("HobgoblinLV5"), Mob("GoblinLV1"), Mob("GoblinLV1"), Mob("GoblinLV1"), Mob("GoblinLV1"),
                        Mob("GoblinLV1")]
custom_encounter_splash = ["You encounter a lone pair of goblins! One of them flees to raise the alarm, and the other"
                           " turns to fight!", "You have come up on the hobgoblin and five goblins! \"Protect the Soup!"
                                               "\" the hobgoblin bellows"]
custom_encounters = [first_guard, chapel_confrontation]
custom_encounter_names = ["first_guard", "chapel_confrontation"]


class Encounter:
    def __init__(self, encounter_level, enemy_pool: str,
                 custom_name: str):  # custom encounters are encounters specially
        # crafted by yours truly
        self.encounter_level = encounter_level
        self.enemies = []
        self.custom_index = None
        # a pool has an enemy pool name or custom name, not both.
        if enemy_pool != "":
            for i in range(len(pool_names)):
                if pool_names[i] == enemy_pool:
                    self.mob_pool = mob_pools[i]
                    break
            budget = 0  # the budget is how many levels of enemy we get
            while budget < self.encounter_level:
                selection = random.randint(0, len(self.mob_pool) - 1)
                new_mob = self.mob_pool[selection]
                self.enemies.append(new_mob)
                budget += new_mob.level
        elif custom_name != "":
            for i in range(len(custom_encounters)):
                if custom_encounter_names[i] == custom_name:
                    self.enemies = custom_encounters[i]
                    self.custom_index = i
                    break

    def __str__(self):
        if self.custom_index is None:
            output = "You encounter enemies!\n"
            for i in range(len(self.enemies)):
                output += self.enemies[i].name + "\n"
        else:
            output = custom_encounter_splash[self.custom_index] + "\n"
            for i in range(len(self.enemies)):
                output += self.enemies[i].name + "\n"
        return output


def test():
    first_guard_encounter = Encounter(1, "", "first_guard")
    middle_encounter_1 = Encounter(3, "dilapidated_chapel", "")
    middle_encounter_2 = Encounter(5, "dilapidated_chapel", "")
    middle_encounter_3 = Encounter(8, "dilapidated_chapel", "")
    chapel_confrontation_encounter = Encounter(10, "", "chapel_confrontation")
    print(str(first_guard_encounter) + "\n")
    print(str(middle_encounter_1) + "\n")
    print(str(middle_encounter_2) + "\n")
    print(str(middle_encounter_3) + "\n")
    print(str(chapel_confrontation_encounter))


test()
