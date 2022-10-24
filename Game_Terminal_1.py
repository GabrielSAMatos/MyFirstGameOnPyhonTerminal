<<<<<<< HEAD
=======
from time import sleep 

#1 = device, white/gray
#2 = fight, white/red
#3 = place, blue/green
#4 = secret, blue
#5 = items, pink/blue
#6 = black/red
#7 = chest, black/yellow

>>>>>>> main
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
<<<<<<< HEAD
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
=======
    else:
        print(f'\033[7;49;33{msg}\033[m')
>>>>>>> main


def game_over():
    chain()
    print(f'\033[7;49;91m{"Game Over":^92}\033[m', end='')
    chain()
    exit()


<<<<<<< HEAD
def invalid():
    colors('ERROR. Invalid Alternative!', 'redw')
=======
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
>>>>>>> main


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


<<<<<<< HEAD
def forest(woods='start'):
    if woods == 'start':
=======
def short_line():
    line = '~'*15
    colors(line, 4)


def forest_begin(x=''):
    """
    Just the initial scenario.
    """
    if x == '':
>>>>>>> main
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○ ⩀  ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
<<<<<<< HEAD
    elif woods == 'nap1':
=======
    elif x == 'nap1':
>>>>>>> main
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀Zz ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
<<<<<<< HEAD

    elif woods == 'nap2':
=======
    elif x == 'nap2':
>>>>>>> main
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀Zz ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森Zz  /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
<<<<<<< HEAD
    elif woods == 'nap3':
=======
    elif x == 'nap3':
>>>>>>> main
        forest = '\033[7;49;91m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森s森森森森森森森 森森森森森\
森森森森森森森森森森森森森森森森森森森森○⩀↞Ÿ ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森Ÿ↟  ↞Ÿ⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|Ÿ↟|森森森森森森森森森森森森森森森森森森森森森森\033[m'
<<<<<<< HEAD
    elif woods == 'move on':
        forest = '\033[7;49;92m森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森森森森 森森森森森\
=======
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
>>>>>>> main
森森森森森森森森森森森森森森森森森森森森○   ⊞ 森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森    /⫎森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|. |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|. |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|⩀ |森森森森森森森森森森森森森森森森森森森森森森森森\
<<<<<<< HEAD
森森森森森森森森森森森森森森森森森森森森|  .|森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
    print(forest)


def chest(status):
    """
    Just the view of the chest
    """
    if status == 'closed':
        colors('____________________________________________________________________________________________\
=======
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森森\
森森森森森森森森森森森森森森森森森森森森|  |森森森森森森森森森森森森森森森森森森森森森森森\033[m'
    print(f'\n{forest}')


def chest(c=0):
    """
    Just the view of the chest
    """
    if c == 0:
        chest = '\033[;49;33m____________________________________________________________________________________________\
>>>>>>> main
|==========================================================================================|\
|===================================________________=======================================\
|||||||||||||||||||||||||||||||||||||     ⌈    ⌉     ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||     ⌊ ⁐  ⌋     ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||_____⌊____⌋_____||||||||||||||||||||||||||||||||||||||||\
|==========================================================================================|\
<<<<<<< HEAD
--------------------------------------------------------------------------------------------', 'yellow')
    elif status == 'with_key':
        colors('____________________________________________________________________________________________\
=======
--------------------------------------------------------------------------------------------\033[m'
    elif c == 1:
        chest = '\033[;49;33m____________________________________________________________________________________________\
>>>>>>> main
|==========================================================================================|\
|==========================================================================================\
|||||||||||||||||||||||||||||||||||||        |⁅      ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||        Ⅲ       ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||      O|⁐⁐ |O   ||||||||||||||||||||||||||||||||||||||||\
|==========================================================================================|\
<<<<<<< HEAD
--------------------------------------------------------------------------------------------', 'yellow')
    elif status == 'without':
        colors('____________________________________________________________________________________________\
=======
--------------------------------------------------------------------------------------------\033[m'
    elif c == 2:
        chest = '\033[;49;33m____________________________________________________________________________________________\
>>>>>>> main
|==========================================================================================|\
|==========================================================================================\
|||||||||||||||||||||||||||||||||||||                ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||                ||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||                ||||||||||||||||||||||||||||||||||||||||\
|==========================================================================================|\
<<<<<<< HEAD
--------------------------------------------------------------------------------------------', 'yellow')

=======
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
    
>>>>>>> main

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
<<<<<<< HEAD
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
=======


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
>>>>>>> main
        elif choice == 'nap':
            nap(nap_times)
        else:
<<<<<<< HEAD
            invalid()

=======
            erro()
>>>>>>> main

def chest_without_key():
    while True:
        sleep(1.5)
        chest('without')
        line(LINE_SIZE)
        colors('Empty.', 'gray')
        colors('(go back)\n(cry)', 'cyan')
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
<<<<<<< HEAD
        forest('nap1')
        colors("*now woke up*\nYou don't know if you're more tired or more willing", 'gray')
        line(SHORT_LINE_SIZE)
        return 
    elif (len(nap_times)) == 2:
        sleep(1.5)
        colors('Zzzzzzzzzzzzzzz','gray')
        forest('nap2')
        colors('*now woke up*\nYou almost fell asleep again', 'gray')
        line(SHORT_LINE_SIZE)
        return 
    elif (len(nap_times)) == 3:
        sleep(1.5)
        forest('nap3')
        chain()
=======
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
>>>>>>> main
        print('\033[7;49;91mYou fell into such a deep sleep that the Caucaia tribe,\
 known as the "papangus", took you!  ')
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

<<<<<<< HEAD
start()
introduction()
beginning()
first_choice()
=======

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
>>>>>>> main
