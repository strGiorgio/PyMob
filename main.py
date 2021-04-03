import os, sys
from func_color import print_wcolor
import main_generate as game
from time import sleep

# funções
def help():
    print_wcolor(35, '=' * 100)
    print_wcolor(33, '''GERAÇÃO - Um mob será gerado com suas habilidade(defesa,força e estamina) aleatórias.\n\nBATALHA - A batalha consiste em 1 inimigo com defesa, força e estamina aleatórias, se a força for mais forte que a defesa dará um dano que resutará na perda de pontos de vidas(hp). A estamina servirá para a regeneração e a quantidade de ataque(hits)''')
    print_wcolor(35, '=' * 100)

# INICIO DO GAME
os.system('cls')
print_wcolor(35, 'BEM VINDO AO JOGO!')

# MENU
while True:
    print_wcolor(36, '[ 1 ] NOVO JOGO\n[ 2 ] COMO JOGAR')

    try:
        escolha = int(input('>>> '))
        os.system('cls')
    except(ValueError):
        os.system('cls')
        print_wcolor(31, "Opção não disponivel! Tente novamente.")
        continue

    if escolha <= 0:
        print_wcolor(31, "Opção não disponivel! Tente novamente.")
    elif escolha >= 3:
        print_wcolor(31, "Opção não disponivel! Tente novamente.")

        
    if escolha == 1:
        while True:
            print_wcolor(36, '[ 1 ] GERAR MOB ALEATÓRIO\n[ 2 ] MOB PRÉ-DEFINIDO')

            try:
                escolha_2 = int(input('>>> '))
                os.system('cls')
            except(ValueError):
                os.system('cls')
                print_wcolor(31, "Opção não disponivel! Tente novamente.")
                continue

            if escolha_2 <=  0:
                print_wcolor(31, "Opção não disponivel! Tente novamente.")
            elif escolha_2 >= 3:
                print_wcolor(31, "Opção não disponivel! Tente novamente.")


            if escolha_2 == 1:
                while True:
                    nameL = list()
                    print_wcolor(36, 'Escolha o nome do seu mob:')
                    name = (input('>>> '))
                    os.system('cls')
                
                    for l in name:
                        nameL.append(l)

                    if name.isnumeric():
                        print_wcolor(31, 'Nome com números? Por favor tente novamente')
                        continue
                    elif len(nameL) < 2:
                        print_wcolor(31, 'Nome muito curto!')
                        continue
                    
                    mob = game.generate()
                    mob.generate_mob(name)
                    mob.enemy_generate()
                    mob.init_battle()
                    break 

            elif escolha_2 == 2:
                print_wcolor(31, "Opção não disponivel! Tente novamente.")
                continue

    elif escolha == 2:
        os.system('cls')
        help()

