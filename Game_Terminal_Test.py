#tree: 森
#rock: ○
#person: ⩀
#chest: ⊞
#papangu: Ÿ
#steel: ↟
from time import sleep
SHORT_LINE_SIZE=15
LINE_SIZE=46
nap_times = []
chest_0 = ['ŧ']

def colors(msg, color='black'):
    if color == 'blue': 
        print(f'\033[7;49;94m{msg}\033[m ')
    elif color == 'redw':
        print(f'\033[7;49;31m{msg}\033[m ')
    elif color == 'green':
        print(f'\033[7;49;92m{msg}\033[m ')
    elif color == 'black':
        print(f'\033[5;49;34m{msg}\033[m ')
    elif color == 'pink':
        print(f'\033[7;49;95m{msg}\033[m ')
    elif color == 'redb':
        print(f'\033[7;49;91m{msg}\033[m')
    elif color == 'gray':
        print(f'\033[7;49;90m{msg}\033[m')
    elif color == 'cyan':
        print(f'\033[0;49;96m{msg}\033[m')
    elif color == 'yellow':
        print(f'\033[;49;33m{msg}\033[m')


def line(size=LINE_SIZE):
    colors('=~'*size, 'black')


def chain(size=LINE_SIZE):
    colors('-='*size, 'redb')


def game_over():
    chain()
    print(f'\033[7;49;91m{"Game Over":^92}\033[m', end='')
    chain()
    exit()


def invalid():
    colors('ERROR. Invalid Alternative!', 'redw')


def start():
    while True:
        play = input('Start Game? [Start/Exit]\n').lower()
        if play == 'start':
            line()
            return 
        elif play == 'exit':
            print(':(')
            exit()
        else: 
            print('Please type "Start" or "Exit" to continue.')


def forest(woods='start'):
    if woods == 'start':
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀   ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
    elif woods == 'nap1':
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀Zz ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'

    elif woods == 'nap2':
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀Zz ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森Zz  /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
    elif woods == 'nap3':
        forest = '\033[7;49;91m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森s森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀↞Ÿ ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森Ÿ↟  ↞Ÿ⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森\033[m'
    elif woods == 'move on':
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○   ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|. |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|. |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|⩀ |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
    elif woods == 'chest':
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○   ⩀⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
    print(forest)


def chest(status):
    """
    Just the view of the chest
    """
    if status == 'closed':
        colors('____________________________________________________________________________________________\
|==========================================================================================|\
|===================================________________=======================================\
|||||||||||||||||||||||||||||||||||||     ⌈    ⌉     ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||     ⌊ ⁐  ⌋     ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||_____⌊____⌋_____||||||||||||||||||||||||||||||||||||||||\
|==========================================================================================|\
--------------------------------------------------------------------------------------------', 'yellow')
    elif status == 'with_key':
        colors('____________________________________________________________________________________________\
|==========================================================================================|\
|==========================================================================================\
|||||||||||||||||||||||||||||||||||||        |⁅      ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||        Ⅲ       ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||      O|⁐⁐ |O   ||||||||||||||||||||||||||||||||||||||||\
|==========================================================================================|\
--------------------------------------------------------------------------------------------', 'yellow')
    elif status == 'without':
        colors('____________________________________________________________________________________________\
|==========================================================================================|\
|==========================================================================================\
|||||||||||||||||||||||||||||||||||||                ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||                ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||                ||||||||||||||||||||||||||||||||||||||||\
|==========================================================================================|\
--------------------------------------------------------------------------------------------', 'yellow')


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
    line(LINE_SIZE)    


def introduction():     
    introduction = """You wake up in a forest.                                                                   |
Behind you is a very large rock, it is still daylight.                                     |
You only have the clothes on your body, a blouse, pants and shoes (all cloth).             |
To your left is just a dense forest.                                                       |
To your right is a chest.                                                                  |
And in front of you is a road.'                                                            |"""
    colors(introduction, 'blue')
    line()
    sleep(8)


def beginning():
    beginning = """Theres not much to do.                                                                     |
You want to move on.                                                                       |
Examine the chest or remain lying down.                                                    |"""
    colors(beginning, 'blue')
    sleep(5)


def first_choice():
    while True:
        sleep(1.5)
        line(LINE_SIZE)
        forest()
        colors('[move on]\n[examine]\n[nap]', 'cyan')
        choice = input()
        line(SHORT_LINE_SIZE)
        if choice == 'move on':
            move_on()
        if choice == 'examine':
            examine(chest_0)
        elif choice == 'nap':
            nap(nap_times)
        else:
            invalid()


def chest_without_key():
    while True:
        sleep(1.5)
        chest('without')
        line(LINE_SIZE)
        colors('Empty.\n(go back)\n(cry)', 'gray')
        back_or_cry = input()
        if back_or_cry == 'go back':
            return 
        elif back_or_cry == 'cry':
            cry()
            return
        else:
            invalid()


def move_on():
    sleep(1.5)
    forest('move on')
    colors('There are some rocks on the way, but you keep going.', 'gray')
    sleep(5)
    game_over()


def examine(chest_0):
    while True:
        sleep(1.5)
        forest('chest')
        line(LINE_SIZE)
        colors("It's just an old wooden chest. Suspect..", 'gray')
        sleep(1.5)
        chest('closed')
        line(LINE_SIZE)
        colors('(open)\n(go back)', 'cyan')
        open = input()
        line(SHORT_LINE_SIZE)
        if (len(chest_0) > 0) and open == 'open':
            while True:
                sleep(1.5)
                chest('with_key')
                colors('a misteious key', 'pink')
                colors('(take)\n(go back)', 'cyan')   
                key = input()
                line(SHORT_LINE_SIZE)
                if key == 'take':
                    colors('Yout took the key!', 'pink')
                    chest('without')
                    chest_0.pop()
                    return
                elif key == 'go back':
                    return 
                else:
                    invalid()
        elif(len(chest_0) < 1) and open == 'open':
            chest_without_key()
        elif open == 'go back':
            return 
        else:  
            invalid()


def nap(nap_times):
    nap_times.append('↟')
    if len(nap_times) == 1:
        sleep(1.5)
        print('Zzzzzzz')
        forest('nap1')
        colors("*now woke up*\nYou don't know if you're more tired or more willing", 'gray')
        line(SHORT_LINE_SIZE)
        return 
    elif (len(nap_times)) == 2:
        sleep(1.5)
        colors('Zzzzzzzzzzzzz','gray')
        forest('nap2')
        colors('*now woke up*\nYou almost fell asleep again', 'gray')
        line(SHORT_LINE_SIZE)
        return 
    if (len(nap_times)) == 3:
        sleep(1.5)
        forest('nap3')
        chain()
        print('\033[7;49;91mYou fell into such a deep sleep that the Caucaia tribe,\
 known as the "papangus", took you!  ')
        game_over()

start()
introduction()
beginning()
first_choice()
