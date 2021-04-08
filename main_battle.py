from func_color import print_wcolor
from random import randint
import os, sys


class presentation:
    
    def mob(self, name, hp, defense, stamina, strength):
        self.mob_hp = hp
        self.mob_defense = defense
        self.mob_stamina = stamina
        self.mob_strength = strength
        self.mob_name = name

        os.system('cls')
        print('''⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿''')
        space = ""
        level = 0
        print_wcolor(35, '=' * 30)
        print_wcolor(34, f'YOUR MOB HAS BEEN GENERATED!\nNAME: {space * 8}{self.mob_name}\nHP: {space * 10}{self.mob_hp}\nDENFENSE: {space * 4}{self.mob_defense}\nSTAMINA: {space * 5}{self.mob_stamina}\nSTRENGTH: {space * 4}{self.mob_strength}\nLEVEL: {space * 7}{level}')
        print_wcolor(35, '=' * 30)


    def enemy(self, hp, defense, stamina, strength):
        self.enemy_hp = hp 
        self.enemy_defense = defense 
        self.enemy_stamina = stamina 
        self.enemy_strength = strength
        print_wcolor(34, 'Your enemy!')
        print_wcolor(34, f'HP: {self.enemy_hp}, DEFENSE: {self.enemy_defense}, STAMINA: {self.enemy_stamina}, STRENGTH: {self.enemy_strength}')
        

    def start(self, name):
        print_wcolor(35, "=" * 30)
        while True:
            try:
                print_wcolor(36, "[ 1 ] START BATTLE \n[ 2 ] RETURN")
                answers = int(input('>>> '))
            except(ValueError):
                os.system('cls')
                print_wcolor(31, 'Option not available! Try again.')
                continue

            if answers == 2:
                os.system('cls')
                break

            elif answers == 1:
                mob_hp = self.mob_hp
                mob_at = self.mob_strength * self.mob_stamina
                mob_def = self.mob_defense
                mob_reg = (self.mob_defense / 5) * self.mob_stamina

                en_hp = self.enemy_hp
                en_at = self.enemy_strength * self.enemy_stamina
                en_def = self.enemy_defense
                en_reg = (self.enemy_defense / 5) * self.enemy_stamina

                while True:
                    try:
                        print_wcolor(36, '[ 1 ] ATTACK\n[ 2 ] REGENERATE')
                        action = int(input('>>> '))
                    except(ValueError):
                        os.system('cls')
                        print_wcolor(31, 'Option not available! Try again.')
                        continue

                    # -----BATTLE----
                    if action == 1:
                        tiredness_1 = randint(1 ,10)
                        tiredness_2 = randint(1 ,10)
                        mob_at = tiredness_1
                        en_at = tiredness_2
                        os.system('cls')
                        en_hp = en_hp - mob_at
                        mob_hp = mob_hp - en_at
                        print_wcolor(35, "=" * 30)
                        print_wcolor(34, f'YOU TOOK {en_at} DAMEGE. YOUR HP: {int(mob_hp)}')
                        print_wcolor(34, f'GIVE {mob_at} DAMAGE. ENEMY HP: {int(en_hp)}')
                        print_wcolor(35, "=" * 30)

                    elif action == 2:
                        mob_hp += mob_reg
                        if mob_hp > 100:
                            mob_hp = 100
                        en_hp += en_reg
                        if en_hp > 100:
                            en_hp = 100
                        os.system('cls')
                        print_wcolor(35, "=" * 50)
                        print_wcolor(34, f'YOU REGENERATED {mob_reg} HP. YOU HP: {int(mob_hp)}')
                        print_wcolor(34, f'YOUR ENEMY REGENERATED {en_reg} HP. ENEMY HP: {int(en_hp)}')
                        print_wcolor(35, "=" * 50)

                    else:
                        os.system('cls')
                        print_wcolor(31, 'Option not available! Try again.')

                    if en_hp <= 0:
                        print_wcolor(33, f'YOU WON! YOUR HP: {int(mob_hp)}')
                        print_wcolor(35, "=" * 50)
                        break
                    elif mob_hp <= 0:
                        print_wcolor(31, f'YOU LOSE! ENEMY HP: {int(en_hp)}')
                        print_wcolor(35, "=" * 30)
                        break
                    
            else:
                os.system('cls')
                print_wcolor(31, 'Option not available! Try again.')