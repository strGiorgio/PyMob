import os, sys
from func_color import print_wcolor
import main_generate as game
from time import sleep

# funções
def help():
    pt_br = '''GERAÇÃO - Um mob será gerado com suas habilidade(defesa,força e estamina) aleatórias.\n\nBATALHA - A batalha consiste em 1 inimigo com defesa, força e estamina aleatórias, a força do hit se resume na força vezes a estamina, a regeneração é a defesa dividido por 5 vezes a estamina\n\nCANSAÇO - Todo rodada tem a chance de 1 a 10 de cansaço, ou seja, seu mob poderá ter um cansaço e dar menos dano mesmo a sua força sendo maior que do inimigo em questão.'''
    en = '''GENERATION - A mob will be generated with your random abilities (defense, strength and stamina).\n\nBATTLE - The battle consists of 1 enemy with random defense, strength and stamina, the strength of the hit is summarized in the strength times the stamina, the regeneration is the defense divided by 5 times the stamina\n\nFATNESS - Every round has a chance of 1 to 10 of tiredness, that is, your mob may be tired and do less damage even though your strength is greater than that of the enemy in question.'''
    print_wcolor(35, '=' * 155)
    print_wcolor(33, en)
    print_wcolor(35, '=' * 155)

    while True:
        try:
            print_wcolor(36, '[ 1 ] TRANSLATE PT-BR\n[ 2 ] RETURN')
            ans = int(input('>>> '))
        except(ValueError):
            os.system('cls')
            print_wcolor(31, 'Option not available! Try again.')
            continue
        if ans == 1:
            os.system('cls')
            print_wcolor(35, '=' * 155)
            print_wcolor(33, pt_br)
            print_wcolor(35, '=' * 155)
            continue
        elif ans == 2:
            os.system('cls')
            break
        else:
            os.system('cls')
            print_wcolor(31, 'Option not available! Try again.')

# INICIO DO GAME
os.system('cls')
print_wcolor(35, 'WELCOME TO THE GAME!')

# MENU
while True:
    print_wcolor(36, '[ 1 ] NEW GAME\n[ 2 ] HOW TO PLAY?')

    try:
        escolha = int(input('>>> '))
        os.system('cls')
    except(ValueError):
        os.system('cls')
        print_wcolor(31, 'Option not available! Try again.')
        continue

    if escolha == 1:
        while True:
            print_wcolor(36, '[ 1 ] GENERATE YOUR MOB\n[ 2 ] PRE-DEFINED MOB \n[ 3 ] RETURN')

            try:
                escolha_2 = int(input('>>> '))
                os.system('cls')
            except(ValueError):
                os.system('cls')
                print_wcolor(31, 'Option not available! Try again.')
                continue

            if escolha_2 == 1:
                while True:
                    nameL = list()
                    print_wcolor(36, 'Choice your mob`s name:')
                    name = (input('>>> '))
                    os.system('cls')
                
                    for l in name:
                        nameL.append(l)

                    if name.isnumeric():
                        print_wcolor(31, 'Name with numbers? Please, try again')
                        continue
                    elif len(nameL) < 2:
                        print_wcolor(31, 'Very short name! Please, try again')
                        continue
                    
                    mob = game.generate()
                    mob.generate_mob(name)
                    mob.enemy_generate()
                    mob.init_battle()
                    break 

            elif escolha_2 == 2:
                os.system('cls')
                print_wcolor(31, 'Option not available! Try again.')
                continue

            elif escolha_2 == 3:
                break

            else:
                os.system('cls')
                print_wcolor(31, 'Option not available! Try again.')

    elif escolha == 2:
        os.system('cls')
        help()

    else:
        os.system('cls')
        print_wcolor(31, 'Option not available! Try again.')

