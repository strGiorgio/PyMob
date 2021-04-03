from func_color import print_wcolor
import os, sys
from random import randint
import main_battle as battle
from time import sleep

class generate:
    def generate_mob(self, name):
        print_wcolor(35, 'GERANDO...')
        sleep(3)

        self.name_mob = name.capitalize()
        self.hp_mob = 100
        self.defense_mob = randint(10, 30)
        self.stamina_mob = randint(1, 5)
        self.strength_mob = randint(1, 10) 
        self.level_mob = 1


    def enemy_generate(self):
        self.hp_enemy = 100
        self.defense_enemy = randint(10, 30)
        self.stamina_enemy = randint(1, 5)
        self.strength_enemy = randint(1, 10) 
        self.level_enemy = 1
        

    def init_battle(self):
        battle_start = battle.presentation()
        battle_start.mob(self.name_mob, self.hp_mob, self.defense_mob, self.stamina_mob, self.strength_mob)
        battle_start.enemy(self.hp_enemy, self.defense_enemy, self.stamina_enemy, self.strength_enemy) 
        battle_start.start(self.name_mob)

    





