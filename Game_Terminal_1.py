from time import sleep 

#1 = device, white/gray
#2 = fight, white/red
#3 = place, blue/green
#4 = secret, blue
#5 = items, pink/blue
#6 = black/red
#7 = chest, black/yellow

#tree: 森
#rock: ○
#person: ⩀
#chest: ⊞


def colors(msg, num):
    if num == 1: 
        print(f'\033[7;49;94m{msg}\033[m ')
    elif num == 2:
        print(f'\033[7;49;31m{msg}\033[m ')
    elif num == 3:
        print(f'\033[7;49;92m{msg}\033[m ')
    elif num == 4:
        print(f'\033[5;49;34m{msg}\033[m ')
    elif num == 5:
        print(f'\033[7;49;95m{msg}\033[m ')
    elif num == 6:
        print(f'\033[7;49;91m{msg}\033[m')
    else:
        print(f'\033[7;49;33{msg}\033[m')


def game_over():
    print('-='*46)
    print(f'\033[7;49;91m{"Game Over":^92}\033[m', end='')
    print('\033[7;49;91m',end ='')
    print('-='*46)
    print('\033[m')
    exit()


def start(msg):
    """
    Beginning of the game
    """
    staart = False
    while not staart:
        start = input(msg).strip().lower()
        if start == 'start':
            begin()
            return 'start'
        elif start == 'exit':
            return 'exit'
        else:
            print('Please, just type "start" or "exit" ')


def erro():
    erro = 'ERROR: Invalid alternative!'
    colors(erro, 6)


def line(x = 0):
    if x == 0:
        line ='=~'*107
        colors(line, 4)
    if x == 1:
        line ='=~'*53
        colors(line, 4)       


def short_line():
    line = '~'*15
    colors(line, 4)


def forest_begin(x=''):
    """
    Just the initial scenario.
    """
    if x == '':
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○ ⩀  ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
    elif x == 'nap1':
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀Zz ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
    elif x == 'nap2':
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀Zz ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森Zz  /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
    elif x == 'nap3':
        forest = '\033[7;49;91m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森s森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀↞Ÿ ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森Ÿ↟  ↞Ÿ⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森\033[m'
    elif x == 'examine':
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○   ⩀⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
    elif x == 'move on':
                forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○   ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|. |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|. |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|⩀ |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
    print(f'\n{forest}')


def chest(c=0):
    """
    Just the view of the chest
    """
    if c == 0:
        chest = '\033[;49;33m____________________________________________________________________________________________\
|==========================================================================================|\
|===================================________________=======================================\
|||||||||||||||||||||||||||||||||||||     ⌈    ⌉     ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||     ⌊ ⁐  ⌋     ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||_____⌊____⌋_____||||||||||||||||||||||||||||||||||||||||\
|==========================================================================================|\
--------------------------------------------------------------------------------------------\033[m'
    elif c == 1:
        chest = '\033[;49;33m____________________________________________________________________________________________\
|==========================================================================================|\
|==========================================================================================\
|||||||||||||||||||||||||||||||||||||        |⁅      ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||        Ⅲ       ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||      O|⁐⁐ |O   ||||||||||||||||||||||||||||||||||||||||\
|==========================================================================================|\
--------------------------------------------------------------------------------------------\033[m'
    elif c == 2:
        chest = '\033[;49;33m____________________________________________________________________________________________\
|==========================================================================================|\
|==========================================================================================\
|||||||||||||||||||||||||||||||||||||                ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||                ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||                ||||||||||||||||||||||||||||||||||||||||\
|==========================================================================================|\
--------------------------------------------------------------------------------------------\033[m'
    elif c == 3:
        chest = ("""
 \033[;49;33m____________
|    |⁅      |
|    Ⅲ       |
|  O|⁐⁐ |O   |
|------------|\033[m
""")
    print(chest)
    

def cry():
    print("""
\033[7;49;95m=======-=-=-=-=-=-=-=-=-=-=
|    --´       `--     |
|     O        O       |
|     ✻       ✻        |
|    ✻    ֏₸    ✻  ✻   |
|                      |
|      _______         |
|     /       \        |
========================\033[m
""")


def begin():
    """
    Only Text.
    """     
    begin= "You wake up in a forest. \
Behind you is a very large rock, it is still daylight. \
You only have the clothes on your body, a shirt, pants and shoes (all cloth). \
To your left is just a dense forest. \
To your right is a chest. \
And in front of you is a road."
    colors(begin,1)
    line()
    


def begin_1(fa):
    if fa == 'exit':
        print(':(')
        exit()
    else:
        begin_1 = 'Theres not much to do. \
You want to move on. \
Examine the chest or remain lying down?'
    colors(begin_1,1)


def begin_choice():
    sucess = False
    cont_nap = 0
    forest_begin()
    while not sucess:
        line(1)
        msg = '(move on)\n(examine)\n(nap)\n'
        choice = input(msg)
        short_line()
        if choice == 'move on':
            sleep(2)
            print('You go on along the trail')
            return 'move on'
        elif choice == 'examine':
            print('You approach the chest')
            sleep(2)
            return 'examine'
        elif choice == 'nap':
            cont_nap += 1
            nap(cont_nap)
            continue
        else:
            erro()


#=========================================================
def nap(cont_nap):
    cont_nap += 1
    sleep(1)
    if cont_nap == 2:
        print('Zzzzzzz')
        forest_begin('nap1')
        print("*now woke up*\nYou don't know if you're more tired or more willing")
        short_line()
        return 
    elif cont_nap == 3:
        colors('Zzzzzzzzzzzzz',7)
        forest_begin('nap2')
        print('*now woke up*\nYou almost fell asleep again')
        short_line()
        return 
    if cont_nap == 4:
        forest_begin('nap3')
        print('\033[7;49;91mYou fell into such a deep sleep that the Caucaia tribe,\
 known as the "papangus", took you!')
        game_over()
    

def examine(key):  
    forest_begin('examine')
    sleep(2)
    line()
    cont = 0
    chest()
    print("It's just an old wooden chest. Suspect..")
    for c in range (3):
        short_line()
        answer = input('(open)\n(go back)\n')
        short_line()
        if answer == 'open':
            for cont in range(3):
                    if (len(key)) > 0:
                        sleep(2)
                        chest(1)
                        sleep(2)
                        print(f'a mysterious key.')
                        short_line()
                        pick = input('(take)\n(go back)\n')
                        short_line()
                        if pick == 'take':
                            sleep(1)
                            key.remove('key')
                            print('\nYou took the key')  
                            short_line()
                            sleep(1) 
                            chest(3)
                            sleep(1)
                            return key
                        elif pick == 'go back':
                            sleep(2)
                            begin_choice()
                        else:
                            erro()
                    else:
                        sleep(2)
                        chest(2)
                        short_line()
                        pick = input('Empty.\n(go back)\n(cry)\n')
                        short_line()
                        if pick == 'go back':
                            sleep(2)
                            begin_choice()
                        elif pick == 'cry':
                            sleep(2)
                            cry()
                            sleep(2)
                            return
                        else:
                            erro()                     
        elif answer == 'go back':
            pass
            
        else:
            erro()
            
        
def movie_on():
    forest_begin('move on')


obj = ['key']
Start = start('Start Game? ')
begin_1(Start)
fisrt_awser = begin_choice()
while True:
    if fisrt_awser == 'examine':
        key=examine(obj)
        second_awser = begin_choice()
        if second_awser == 'move on':
            movie_on()
            break
    else:
        movie_on()
        break

#Need to finish "move onX" and "examine✓" options. \
#Remember to be able to go back to the beginning after moving forward!