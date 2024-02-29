# a group of mobs, encountered together, in one room.
from mob import Mob
import random

# these are all the pools of possible mobs in an encounter
dilapidated_chapel = [Mob("GoblinLV1"), Mob("Monopod"), Mob("GiantRat")]
mob_pools = [dilapidated_chapel]
pool_names = ["dilapidated_chapel"]

first_guard = [Mob("GoblinLV1")]
custom_encounters = [first_guard]
custom_encounter_names = ["first_guard"]


class Encounter:
    def __init__(self, encounter_level, enemy_pool: str,
                 custom_name: str):  # custom encounters are encounters specially
        # crafted by yours truly
        self.encounter_level = encounter_level
        self.enemies = []
        # a pool has an enemy pool name or custom name, not both.
        if enemy_pool != "":
            for i in range(len(pool_names)):
                if pool_names[i] == enemy_pool:
                    self.mob_pool = mob_pools[i]
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

    def __str__(self):
        output = "You encounter enemies!\n"
        for i in range(len(self.enemies)):
            output += self.enemies[i].name + "\n"
        return output


def test():
    test_encounter = Encounter(5, "dilapidated_chapel", "")
    print(str(test_encounter))


test()
