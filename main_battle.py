from func_color import print_wcolor
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
        print_wcolor(36, "[ 1 ] INICIAR BATALHA")
        input('>>> ')

    def battle(self):
        mob_hp = self.mob_hp
        mob_at = self.mob_strength * self.mob_stamina
        mob_def = self.mob_defense
        mob_reg = (self.mob_defense / 5) * self.mob_stamina

        en_hp = self.enemy_hp
        en_at = self.enemy_strength * self.enemy_stamina
        en_def = self.enemy_defense
        en_reg = (self.enemy_defense / 5) * self.enemy_stamina

        