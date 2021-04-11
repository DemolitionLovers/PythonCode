import os
import sys
import time
import random
import string
import requests



## 2019-12-12 18:26: All seems complete and program now seems to be at a sort of 'Alpha' release stage.



def PlayAgain(in_text):  #  Function to ask user if they want to play the game again.
    play_ask = False
    while play_ask != True:
        play_again = input(f'{in_text} (y/N): ')
        if play_again.lower() == 'y':
            play_ask = True
            main()  #  Call the main function to reset everything and run it from the start all over again.
        elif play_again.lower() == 'n':
            play_ask = True
            goodbye_message = """
                                              
   ______                ____               __
  / ____/___  ____  ____/ / /_  __  _____  / /
 / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ / 
/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/  
\____/\____/\____/\__,_/_.___/\__, /\___(_)   
                             /____/           
                         A game by xxxx xxxxx
                                     (xxxxxxx)

"""
            for char in list(goodbye_message):
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.001)

            print() 

            time.sleep(.5)
            exit()



def NewsToday():  #  A function to attempt to entertain the player with a news headline from BBC News.
    ## use these headers to pretend to be a Firefox web browser when making requests
    HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.5',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
    }

    ##  BBC NEWS URL
    ##   This is the BBC News URL; becuase it should not cause controversy like 4chan or similar.
    ##   It should be a, generally, politically correct source of headlines.
    url = 'https://www.bbc.co.uk/news'

    ##  Request the url 'as a browser'.
    r = requests.get(url, timeout=3, headers=HEADERS)  # if it takes more than 3 seconds, give up on it...

    ##  Split the page. (for iteration)
    page = r.text
    splitlines_list = [
        '<',
        '>',
        '"',
        '&#x27;',
    ]
    for item in splitlines_list:
        page = page.replace(item, f'\n{item}\n')
    page = page.splitlines()

    ##  Find a headline from the page.
    whitelist_strings = [
        'brexit',
        'trump',
        'johnson',
        'china',
    ]
    blacklist_strings = [
        'http',
        '/',
        '?',
        ';',
        '&',
    ]
    topic = random.choice(whitelist_strings)
    for line in page:
        if topic in line  or  topic.upper() in line  or topic.capitalize() in line:
            blacklist_checks = 0
            for check in blacklist_strings:
                if  check not in line  and  check.capitalize() not in line  and  check.upper() not in line:
                    blacklist_checks += 1
                if blacklist_checks == len(blacklist_strings):  #  If all checks were passed i.e no blacklist word found.
                    return line
    #  If the above fails to find anything... return an empty string.
    return ''




def ReadScoresFile():  #  A function to read and write to an external scores file. (for persistant score keeping)
    ##  Reading from this file and using its contents seems like a potential vulnerability. (attack vector)
    ##  I don't yet know how to security-patch this; I have had no experience writing security patches yet.
    readfile = 'lsd-scores.log'
    try:
        with open(readfile, 'a') as f:
            f.write('')   #  If the file does not exist, create it. If the file exists, add nothing to it yet.
        with open(readfile, 'r') as f:  #  The contents of this read seem to require a 'normalized' logfile.
            split_file = f.read().splitlines()


            all_scores = []
            for index, line in enumerate(split_file):  #  Get a sorted list of all the scores available.
                if int(line.split()[5]) < 0: line.split()[5] = str(0)
                all_scores.append(line.split()[5])
            number_prints = 0
            potential_score = 300  #  Highest possible score. (declared at 20191202 12:47)
            sorting_scores_list = []
            while  (potential_score >= 0)  and  (number_prints < 30):
                for index, each in enumerate(all_scores): # ? :/
                    try:
                        if int(each) == int(potential_score):
                            sorting_scores_list.append(split_file[index])
                            number_prints += 1 # (only on prints, we are tracking printed lines here!)
                    except:
                        pass
                potential_score -= 1  #  Iterate the value of 'potential_score' down by 1.

        modes_list = ['Hard Mode', 'Medium Mode', 'Easy Mode']
        print()
        ClearFunction()  #  Clear screen before printing high scores.
        high_scores_ascii = """
8       o        8                                                 
8                8                                                 
8oPYo. o8 .oPYo. 8oPYo.   .oPYo. .oPYo. .oPYo. oPYo. .oPYo. .oPYo. 
8    8  8 8    8 8    8   Yb..   8    ' 8    8 8  `' 8oooo8 Yb..   
8    8  8 8    8 8    8     'Yb. 8    . 8    8 8     8.       'Yb. 
8    8  8 `YooP8 8    8   `YooP' `YooP' `YooP' 8     `Yooo' `YooP' 
..:::..:..:....8 ..:::..:::.....::.....::.....:..:::::.....::.....:
::::::::::::ooP'.::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::...::::::::::::::::::::::::::::::::::::::::::::::::::::
"""
        print(high_scores_ascii)
        input('< press enter to continue... >\n')
        for mode in modes_list:
            ClearFunction()
            print(f'::| ~ ~ ~ [ {mode.upper()} ] ~ ~ ~ |::\n')  #  Print title/seperator for each mode.
            place_number = 1   #  Start at 1, for each mode.
            for item in sorting_scores_list:
                if mode in item:
                    item = item.split()
                    if place_number < 10:
                        time.sleep(.05)
                        print(f'  #{place_number}: {item[0]} --- {item[5]}')
                        place_number += 1
                    elif place_number == 10:
                        time.sleep(.05)
                        print(f' #{place_number}: {item[0]} --- {item[5]}')
                        place_number += 1
            print()  #  Seperate the output of different modes.
            input(' *** ')
    except:
        print(f'< Error reading "{readfile}" file >')
        pass

    time.sleep(.2)
    PlayAgain('Play the game?')






def ClearFunction():  # This function tries to check for the operating system so it can clear the terminal.
    if sys.platform.startswith('win32'):
        os.system('cls')    #  For Windows.
    elif sys.platform.startswith('os2'):
        os.system('cls')    #  For OS/2.
    elif sys.platform.startswith('os2emx'):
        os.system('cls')    #  For OS/2 EMX.
    elif sys.platform.startswith('linux'):
        os.system('clear')  #  For Linux.
    elif sys.platform.startswith('darwin'):
        os.system('clear')  #  For Mac?  (unable to check due to financial constraints)






def Winner():  #  A function to run when the player reaches the winning game-spot.
    win_chance = random.randint(0,6)

    if current_player.mode == 'E':
        odds_num = 0

    elif current_player.mode == 'M':
        odds_num = 2
        if current_player.item == '':
            print('As you wonder through the abyss of mere existence, you realise a terrifying monster in the shadows...')
            print('Completely unprepared for this experience, you fall ever-deeper into its beastly grasp.')
            input('\n< press enter to continue... >\n')
            Death()  #  Player dies if they have no item.
        elif current_player.item == 'sword':
            print('As you wonder through the abyss of mere existence, you realise a terrifying monster in the shadows...')
            print(f'You swing your {current_player.item} at it, but it is unaffected by this and it seems to follow you everywhere you go!')
            input('\n< press enter to continue... >\n')
            Death()  #  Player dies if they have the *sword* item.
        elif current_player.item == 'pen':
            print('As you wonder through the abyss of mere existence, you realise a terrifying monster in the shadows...')
            print(f'You write down a description of this beast with your {current_player.item}, and its presence seems to somewhat lessen.')
            print('You seem able to continue... but these issues are left in the shadows, where they burden you forevermore.')
            current_player.score -= 19  #  Player loses 19 score points if they have the *pen* item.
            input('\n< press enter to continue... >\n')
            #    (And let it continue)
        elif current_player.item == 'keyboard':
            print('As you wonder through the abyss of mere existence, you realise a terrifying monster in the shadows...')
            print(f'You type a description of this beast on your {current_player.item}, and its presence seems to somewhat lessen.')
            print('As you examine it more closely, it seems to be an unintegrated issue from the playground of your youth!')
            print('Over the period of a few days, you begin to integrate these dark aspects of your character into your conscious idea of your very being.')
            input('\n< press enter to continue... >\n')
            #  Player loses no points, and does not die if they have the *keybaord* item.
            #    (And let it continue)

    elif current_player.mode == 'H':
        odds_num = 4
        if current_player.item == '':
            print('As you wonder through the abyss of mere existence, you realise a terrifying monster in the shadows...')
            print('Completely unprepared for this experience, you fall ever-deeper into its beastly grasp.')
            input('\n< press enter to continue... >\n')
            Death()  #  Player dies if they have no item.
        elif current_player.item == 'sword':
            print('As you wonder through the abyss of mere existence, you realise a terrifying monster in the shadows...')
            print(f'You swing your {current_player.item} at it, but it is unaffected by this and it seems to follow you everywhere you go!')
            input('\n< press enter to continue... >\n')
            Death()  #  Player dies if they have the *sword* item.
        elif current_player.item == 'pen':
            print('As you wonder through the abyss of mere existence, you realise a terrifying monster in the shadows...')
            print(f'You write down a description of this beast with your {current_player.item}, and its presence seems to somewhat lessen.')
            print('It eventually becomes too much to record completely...')
            input('\n< press enter to continue... >\n')
            Death()  #  Player dies if they have the *pen* item.
        elif current_player.item == 'keyboard':
            print('As you wonder through the abyss of mere existence, you realise a terrifying monster in the shadows...')
            print(f'You type a description of this beast on your {current_player.item}, and its presence seems to somewhat lessen.')
            print('As you examine it more closely, it seems to be an unintegrated issue from the playground of your youth!')
            print('Over the period of a few days, you begin to integrate these dark aspects of your character into your conscious idea of your very being.')
            input('\n< press enter to continue... >\n')
            #  Player loses no points, and does not die if they have the *keybaord* item.
            #    (And let it continue)

    if win_chance > odds_num:
        print('You appear to have been in the right place at the right time...           ...this time.')
        print('After five or six hours of wondering around mountains, valleys, meadows, caves,', end='')
        print('and so on, you find yourself in your back garden with an empty cup of tea.\nWhat a perculiar and awe-inspiring daydream...', end='')
        print(' ' * round(os.get_terminal_size().columns / 3), end='')
        time.sleep(.4)
        print(('\n' * 2) + f'CONGRATULATIONS, {current_player.name}! You resolved this chaotic experience and returned to your regular, every-day egoic state!')
        time.sleep(1.2)
        winning_ascii_art = """
        ______ _            ___               
       (_) |  | |          / (_)           |  
           |  | |     _    \__   _  _    __|  
    <3   _ |  |/ \   |/    /    / |/ |  /  |   <3
        (_/   |   |_/|__/  \___/  |  |_/\_/|_/"""
        print(winning_ascii_art)
        time.sleep(1.2)

        if current_player.score < 0:
           current_player.score = 0

        print()
        win_message_1 = 'You Win'
        win_message_2 = 'Thank you for playing!'
        win_message_3 = 'Your score was: '
        win_message_4 = str(current_player.score)

        for char in list(win_message_1):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(random.uniform(.005,.3))

        print() 
        time.sleep(1.2)

        for char in list(win_message_2):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(random.uniform(.005,.3))

        if current_player.mode == 'E': full_mode = 'Easy Mode'
        elif current_player.mode == 'M': full_mode = 'Medium Mode'
        elif current_player.mode == 'H': full_mode = 'Hard Mode'
        with open(scorekeeper_log, 'a') as f:
            if current_player.score < 0:
                current_player.score = 0
            f.write(f'{current_player.name} : {full_mode} : {current_player.score}\n')

        print() 
        time.sleep(1.2)

        for char in list(win_message_3):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(random.uniform(.005, .3))

        time.sleep(1.2)

        for char in list(win_message_4):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(random.uniform(.015, .9))

        print('\n') 
        time.sleep(2.4)
        PlayAgain('Play again?')

    else:
        ClearFunction()
        time.sleep(.3)
        print('You seemed oddly close to winning something somehow just there... However, there has been a mixup in the dream-space as you suffered from deja-vu....')
        print('You feel this place to be more and more familiar somewhat as you get closer, and closer.\n')
        if current_player.mode == 'E' and current_player.score > 0: current_player.score -= 3
        if current_player.mode == 'M' and current_player.score > 0: current_player.score -= 19
        if current_player.mode == 'H' and current_player.score > 0: current_player.score -= 99
        input('< press enter to continue... >\n')
        ClearFunction()
        StartValleyEasy()






def Death():  #  A function to run when the player reaches a death/losing game-spot.
    print('-' * os.get_terminal_size().columns)
    print('You find yourself examining a dark abyss-like spectre in the sky.', end=' ')
    print('The harder you stare, the harder it stares back with its odd metaphorical grimace.')
    print(' ...After deep contemplation about the issue, you come to realise that you lack the will to continue and you slowly die from exposure.')
    print(' ' * round(os.get_terminal_size().columns / 3), end='')

    time.sleep(1)
    deadcow_ascii_art1 = """
    _   _       @@@@@@@   @@@@@@  @@@@@@@@@@  @@@@@@@@
   ((___))    !@@       @@!  @@@ @@! @@! @@! @@!     
   [ x x ]    !@! @!@!@ @!@!@!@! @!! !!@ @!@ @!!!:!  
    \   /     :!!   !!: !!:  !!! !!:     !!: !!:     
    (' ')      :: :: :   :   : :  :      :   : :: :::
     (U)"""
    deadcow_ascii_art2 = """
            @@@@@@  @@@  @@@ @@@@@@@@ @@@@@@@ 
           @@!  @@@ @@!  @@@ @@!      @@!  @@@
           @!@  !@! @!@  !@! @!!!:!   @!@!!@! 
           !!:  !!!  !: .:!  !!:      !!: :!! 
            : :. :     ::    : :: :::  :   : :"""

    print(deadcow_ascii_art1)
    time.sleep(1)
    print(deadcow_ascii_art2)
    time.sleep(1)

    print('\nYou Lose.')
    current_player.score = 0  # Score becomes 0, because the player died.

    if current_player.mode == 'E': full_mode = 'Easy Mode'
    elif current_player.mode == 'M': full_mode = 'Medium Mode'
    elif current_player.mode == 'H': full_mode = 'Hard Mode'
    with open(scorekeeper_log, 'a') as f:
        if current_player.score >= 0:
            f.write(f'{current_player.name} : {full_mode} : {current_player.score}\n')

    time.sleep(.3)
    print(f'Your score was: {current_player.score}')
    time.sleep(.3)
    print()

    time.sleep(1.4)
    PlayAgain('Play again?')






def DifficultyMode():  #  A function to get the user choice of difficulty for their gameplay.
    difficulty_choice = None
    difficulty_list = list('emhEMH')
    while difficulty_choice not in difficulty_list:
        ClearFunction()
        difficulty_choice = input('Select a mode:\n  E : Easy\n  M : Medium\n  H : Hard\n\n  >>> ')
    return difficulty_choice.upper()






def Menu():  #  A function to display a menu for the player.
    headline = None  #  Create this variable ready for logical condition checking.

    while True:
        ClearFunction()
        title_ascii_art = r"""Welcome to the
.___ _                          .___         _____ 
|    |       _____    ____    __| _/   _____/ ____\
|    |       \__  \  /    \  / __ |   /  _ \   __\ 
|    |___     / __ \|   |  \/ /_/ |  (  <_> )  |   
|_______ \  /(____  /___|  /\____ |   \____/|__|   
        \/  \/    \/     \/      \/                
  _________                                     .__   
 /   _____/    __ ________________   ____ _____  |  |  
 \_____  \    |  |  \_  __ \_  __ \_/ __ \\__  \ |  |  
 /        \   |  |  /|  | \/|  | \/\  ___/ / __ \|  |__
/_______  /  /\____/ |__|   |__|    \___  >____  /____/
        \/   \/                         \/     \/      
________                                          
\______ \    _______   ____ _____    _____   ______
 |    |  \   \_  __ \_/ __ \\__  \  /     \ /  ___/
 |    `   \   |  | \/\  ___/ / __ \|  Y Y  \\___ \ 
/_______  /  /\__|    \___  >____  /__|_|  /____  >
        \/   \/           \/     \/      \/     \/ """
        print(title_ascii_art)

        ## NEWS FEATURE
        while headline == None:  # While this variable has not been set with a requested headline.
                try:  #  This is intended primarily for timeouts.
                    headline = NewsToday()
                except:
                    #  If this programming 'tower of babel' fails,
                    #   just pretend it never happened and skip doing the news headline part.
                    pass
        #  Print the headline once a, hopefully, suitable one has been parsed from the requested page  (this seems difficult to check fully)
        if headline is not None  and  headline != '':  #  If a headline was set;
            if len(headline) >= 10:  #  If the headline is 10 characters long or more
                if headline[0] in string.ascii_uppercase:  #  Try to check for only grammatically correct headlines. (Capitalised first character)
                    print(f'\nTEXT SEGMENT FROM BBC NEWS HEADLINE:  "{headline}"\n')  #  Print it out to entertain the user.

        first_loop = True
        display_scores = ''
        while  display_scores.lower() != 'y'  and  display_scores.lower() != 'n':
            if first_loop == False:
                ClearFunction()
                print(title_ascii_art)
                if headline is not None  and  headline != '':  #  If a headline was set;
                    if len(headline) >= 10:  #  If the headline is 10 characters long or more
                        if headline[0] in string.ascii_uppercase:  #  Try to check for only grammatically correct headlines. (Capitalised first character)
                            print(f'\nTEXT SEGMENT FROM BBC NEWS HEADLINE:  "{headline}"\n')  #  Print it out to entertain the user.
            display_scores = input('Display top 10 scores? (y/N): ')
            if display_scores.lower() == 'y':
                ReadScoresFile()
            first_loop = False

        current_player.name = GetName()  #  Set the name the player entered. (this will be UPPERCASE like in old games)
        if current_player.name is not int:
            if current_player.name != None:
                if len(current_player.name) > 0  and  len(current_player.name) <= 20:
                    if current_player.name[0] in string.ascii_letters:
                        break

    current_player.mode = DifficultyMode()  #  Set player's chosen difficulty mode choice.
    current_player.score = ScoreStart()     #  Set player's starting score.

    if current_player.mode == 'E':
        ClearFunction()
        welcome_text = f'Hello {current_player.name}, welcome to this text adventure game!\n'
        print(welcome_text)
        mode_text = '( Easy Mode )'
        print(' ' * (round(len(welcome_text) / 2) - round(len(mode_text) / 2)), end='')
        print(f'{mode_text}\n\n')
    elif current_player.mode == 'M':
        ClearFunction()
        welcome_text = f'Hello {current_player.name}, welcome to this text adventure game!\n'
        print(welcome_text)
        mode_text = '( Medium Mode )'
        print(' ' * (round(len(welcome_text) / 2) - round(len(mode_text) / 2)), end='')
        print(f'{mode_text}\n\n')
    elif current_player.mode == 'H':
        ClearFunction()
        welcome_text = f'Hello {current_player.name}, welcome to this text adventure game!\n'
        print(welcome_text)
        mode_text = '( Hard Mode )'
        print(' ' * (round(len(welcome_text) / 2) - round(len(mode_text) / 2)), end='')
        print(f'{mode_text}\n\n')
    else:
        exit('FATAL ERROR')






def GetName():  #  A function to get the desired username of the player.
    name_string = None
    while name_string == None:
        name_string = None  #  This must be a good name-string at the end, so restarting it here seems good.
        print('Please enter your name...')
        print('    (The name must start with an English alphabet character.)')
        print('    (The name must not be empty.)')
        print('    (MAXIMUM NAME LENGTH IS 20)')
        name_string = input(' >>> ')
        if name_string != None  and  len(name_string) > 0:  #  Check contentful names for problematic characters.
            for char in name_string:  #  For each character in the 'name_string' variable.
                if char not in string.ascii_letters  and  type(char) is int:  # if the character no in alphabet (upper or lowercase) and it is an integer.
                    return  #  End this function by returning nothing.
            name_string = name_string.upper()
            name_string = name_string.replace(' ','_')
            if len(name_string) <= 20:
                if name_string is not int:          # [ These checks seemed clearer when nested on their own lines ] #
                    if name_string != None:
                        if len(name_string) > 0:
                            if name_string[0] in string.ascii_letters:
                                return name_string  #  This only happens if the above checks are passed.
            else:
                name_string = None  #  Else, if variable 'name_string' is None type.
                ClearFunction()     #  Run ClearFunction() function.
        else:
            name_string = None  #  Else, if variable 'name_string' is None type.
            ClearFunction()     #  Run ClearFunction() function.






def ScoreStart():  #  This function sets starting score based on difficulty mode.
    if current_player.mode == 'E':
        score = 100
        return score
    elif current_player.mode == 'M':
        score = 200
        return score
    elif current_player.mode == 'H':
        score = 300
        return score






###########################################
######## [[ EASY MODE FUNCTIONS ]] ########
###########################################
def StartValleyEasy():
    change_position = None
    while change_position not in list('NESWnesw'):  # require correct user input
        ClearFunction()
        print('You find yourself at the bottom of a winding valley.')
        print('The place is strange, with trees that seem to possess an anthropomorphic essence much too real to be a mere dream.')
        print()
        print('To head North up a mountain, enter: N')
        print('To head East downhill, enter: E')
        print('To head South up a mountain, enter: S')
        print('To head West uphill, enter: W')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'N': # Northern Mountain
            ClearFunction()
            NorthMountainEasy()
        elif change_position.upper() == 'E': # East downhill
            ClearFunction()
            EastDownhillEasy()
        elif change_position.upper() == 'S': # Southern Mountain
            ClearFunction()
            SouthMountainEasy()
        elif change_position.upper() == 'W': # West uphill
            ClearFunction()
            WestUphillEasy()


def NorthMountainEasy():
    change_position = None
    while change_position not in list('ewEW'):  # require correct user input
        ClearFunction()
        print('You find yourself upon the northern mountain.')
        print('The clouds up here are moving oddly quickly, and the sky has a magenta hue...')
        print()
        print('To head East along northern the mountain ridge, enter: E')
        print('To head West along northern the mountain ridge, enter: W')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'E':
            ClearFunction()
            print('This path seems to lead somewhere oddly familiar...')

            if current_player.mode == 'E' and current_player.score > 0: current_player.score -= 3
            if current_player.mode == 'M' and current_player.score > 0: current_player.score -= 19
            if current_player.mode == 'H' and current_player.score > 0: current_player.score -= 99

            time.sleep(1)
            print('-' * os.get_terminal_size().columns)
            StartValleyEasy()
            break  #  This is a cautionary 'break' to try to prevent possible recursion issues.
        elif change_position.upper() == 'W': # West uphill
            Death()  # adventurer dies


def EastDownhillEasy():
    change_position = None
    while change_position not in list('nsNS'):  # require correct user input
        ClearFunction()
        print('As you wander down the hill, you notice a meadow appear as the sun comes out.')
        print('A flock of ravens appear to be knocking around here.')
        print('Perhaps this is their day job...')
        print()
        print('To head North where the ravens can watch you closely, enter: N')
        print('To head South towards an odd smell, enter: S')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'N':
            ClearFunction()
            print('This path seems to lead somewhere oddly familiar...')
            time.sleep(1)
            print('-' * os.get_terminal_size().columns)
            StartValleyEasy()
            break  #  This is a cautionary 'break' to try to prevent possible recursion issues.
        elif change_position.upper() == 'S':
            ClearFunction()
            Winner()


def SouthMountainEasy():
    change_position = None
    while change_position not in list('ewEW'):  # require correct user input
        ClearFunction()
        print('You find yourself upon the southern mountain.')
        print('The clouds up here are moving oddly slowly... and the sky has a golden aura!')
        print()
        print('To head West along the sourthern mountain ridge, enter: W')
        print('To head East along the sourthern mountain ridge, enter: E')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'W':
            ClearFunction()
            print('This path seems to lead somewhere oddly familiar...')
            time.sleep(1)
            print('-' * os.get_terminal_size().columns)
            StartValleyEasy()
            break  #  This is a cautionary 'break' to try to prevent possible recursion issues.
        elif change_position.upper() == 'E':
            ClearFunction()
            Winner()


def WestUphillEasy():
    change_position = None
    while change_position not in list('nsNS'):  # require correct user input
        ClearFunction()
        print('After wandering around for a while, you find a dark cave that compells you to enter.')
        print('You enter the cave and cannot find your way back out.')
        print('You come to hear a body of water ahead and somwhere it is rushing dangerously...')
        print()
        print('To head what seems to be North in the dark cave, enter: N')
        print('To head what seems to be South in the dark cave, enter: S')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'N':
            Death()  # adventurer dies
        elif change_position.upper() == 'S':
            ClearFunction()
            print('This path seems to lead somewhere oddly familiar...') # back to Start Valley
            time.sleep(1)
            print('-' * os.get_terminal_size().columns)
            StartValleyEasy()
            break  #  This is a cautionary 'break' to try to prevent possible recursion issues.


#############################################
######## [[ MEDIUM MODE FUNCTIONS ]] ########
#############################################
def StartValleyMedium():
    change_position = None
    while change_position not in list('NESWnesw'):  # require correct user input
        ClearFunction()
        print('You find yourself at the bottom of a winding valley.')
        print('The place is strange, with trees that seem to possess an anthropomorphic essence much too real to be a mere dream.')
        print()
        print('To head North up a mountain, enter: N')
        print('To head East downhill, enter: E')
        print('To head South up a mountain, enter: S')
        print('To head West uphill, enter: W')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'N': # Northern Mountain
            ClearFunction()
            NorthMountainMedium()
        elif change_position.upper() == 'E': # East downhill
            ClearFunction()
            EastDownhillMedium()
        elif change_position.upper() == 'S': # Southern Mountain
            ClearFunction()
            SouthMountainMedium()
        elif change_position.upper() == 'W': # West uphill
            ClearFunction()
            WestUphillMedium()


def NorthMountainMedium():
    change_position = None
    while change_position not in list('ewEW'):  # require correct user input
        ClearFunction()
        print('You find yourself upon the northern mountain.')
        print('The clouds up here are moving oddly quickly, and the sky has a magenta hue...')
        print()
        print('To head East along northern the mountain ridge, enter: E')
        print('To head West along northern the mountain ridge, enter: W')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'E':
            ClearFunction()
            print('This path seems to lead somewhere oddly familiar...')
            time.sleep(1)
            print('-' * os.get_terminal_size().columns)
            StartValleyMedium()
            break  #  This is a cautionary 'break' to try to prevent possible recursion issues.
        elif change_position.upper() == 'W': # West uphill
            Death()  # adventurer dies


def EastDownhillMedium():
    get_item = False
    while get_item != True:
        ClearFunction()
        print('As you wander down the hill, you notice a meadow appear as the sun comes out.')
        print('A flock of ravens appear to be knocking around here.')
        print('Perhaps this is their day job...')
        print()

        print('You also notice a keyboard, a pen, and a sword on the ground')
        print('You feel compelled to pick one of them up, but do you wish to pick up the pen, the keyboard, or the sword?')
        print('Choices:\n    s:sword\n    p:pen\n    k:keyboard')
        print()

        # item_choice = ''  # reset
        item_choice = input(' >>> ')
        sys.stdout.flush()
        sys.stdout.write('\r')
        if  item_choice.lower() == 's'  or  item_choice.lower() == 'sword':
            current_player.item = 'sword'
            get_item = True  # end the loop
        elif  item_choice.lower() == 'p'  or  item_choice.lower() == 'pen':
            current_player.item = 'pen'
            get_item = True  # end the loop
        elif  item_choice.lower() == 'k'  or  item_choice.lower() == 'keyboard':
            current_player.item = 'keyboard'
            get_item = True  # end the loop
    print(f'You picked up the {current_player.item}')
    time.sleep(1)
    print()

    change_position = None
    while change_position not in list('nsNS'):  # require correct user input
        print('To head North where the ravens can watch you closely, enter: N')
        print('To head South towards an odd smell, enter: S')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'N':
            ClearFunction()
            print('This path seems to lead somewhere oddly familiar...')
            time.sleep(1)
            print('-' * os.get_terminal_size().columns)
            StartValleyMedium()
            break  #  This is a cautionary 'break' to try to prevent possible recursion issues.
        elif change_position.upper() == 'S':
            ClearFunction()
            Winner()
        else:
            ClearFunction()


def SouthMountainMedium():
    change_position = None
    while change_position not in list('ewEW'):  # require correct user input
        ClearFunction()
        print('You find yourself upon the southern mountain.')
        print('The clouds up here are moving oddly slowly... and the sky has a golden aura!')
        print()
        print('To head West along the sourthern mountain ridge, enter: W')
        print('To head East along the sourthern mountain ridge, enter: E')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'W':
            ClearFunction()
            print('This path seems to lead somewhere oddly familiar...')
            time.sleep(1)
            print('-' * os.get_terminal_size().columns)
            StartValleyMedium()
            break  #  This is a cautionary 'break' to try to prevent possible recursion issues.
        elif change_position.upper() == 'E':
            ClearFunction()
            Winner()


def WestUphillMedium():
    change_position = None
    while change_position not in list('nsNS'):  # require correct user input
        ClearFunction()
        print('After wandering around for a while, you find a dark cave that compells you to enter.')
        print('You enter the cave and cannot find your way back out.')
        print('You come to hear a body of water ahead and somwhere it is rushing dangerously...')
        print()
        print('To head what seems to be North in the dark cave, enter: N')
        print('To head what seems to be South in the dark cave, enter: S')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'N':
            Death()  # adventurer dies
        elif change_position.upper() == 'S':
            ClearFunction()
            print('This path seems to lead somewhere oddly familiar...') # back to Start Valley
            time.sleep(1)
            print('-' * os.get_terminal_size().columns)
            StartValleyMedium()
            break  #  This is a cautionary 'break' to try to prevent possible recursion issues.


###########################################
######## [[ HARD MODE FUNCTIONS ]] ########
###########################################
def StartValleyHard():
    change_position = None
    while change_position not in list('NESWnesw'):  # require correct user input
        ClearFunction()
        print('You find yourself at the bottom of a winding valley.')
        print('The place is strange, with trees that seem to possess an anthropomorphic essence much too real to be a mere dream.')
        print()
        print('To head North up a mountain, enter: N')
        print('To head East downhill, enter: E')
        print('To head South up a mountain, enter: S')
        print('To head West uphill, enter: W')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'N': # Northern Mountain
            ClearFunction()
            NorthMountainHard()
        elif change_position.upper() == 'E': # East downhill
            ClearFunction()
            EastDownhillHard()
        elif change_position.upper() == 'S': # Southern Mountain
            ClearFunction()
            SouthMountainHard()
        elif change_position.upper() == 'W': # West uphill
            ClearFunction()
            WestUphillHard()


def NorthMountainHard():
    get_item = False
    while get_item != True:
        ClearFunction()
        print('As you wander down the hill, you notice a meadow appear as the sun comes out.')
        print('A flock of ravens appear to be knocking around here.')
        print('Perhaps this is their day job...')
        print()

        print('You also notice a keyboard, a pen, and a sword on the ground')
        print('You feel compelled to pick one of them up, but do you wish to pick up the pen, the keyboard, or the sword?')
        print('Choices:\n    s:sword\n    p:pen\n    k:keyboard')
        print()

        # item_choice = ''  # reset
        item_choice = input(' >>> ')
        sys.stdout.flush()
        sys.stdout.write('\r')
        if  item_choice.lower() == 's'  or  item_choice.lower() == 'sword':
            current_player.item = 'sword'
            get_item = True  # end the loop
        elif  item_choice.lower() == 'p'  or  item_choice.lower() == 'pen':
            current_player.item = 'pen'
            get_item = True  # end the loop
        elif  item_choice.lower() == 'k'  or  item_choice.lower() == 'keyboard':
            current_player.item = 'keyboard'
            get_item = True  # end the loop
    print(f'You picked up the {current_player.item}')
    time.sleep(1)
    print()

    change_position = None
    while change_position not in list('ewEW'):  # require correct user input
        print('You find yourself upon the northern mountain.')
        print('The clouds up here are moving oddly quickly, and the sky has a magenta hue...')
        print()

        print('To head East along northern the mountain ridge, enter: E')
        print('To head West along northern the mountain ridge, enter: W')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'E':
            ClearFunction()
            print('This path seems to lead somewhere oddly familiar...')
            time.sleep(1)
            print('-' * os.get_terminal_size().columns)
            StartValleyHard()
            break  #  This is a cautionary 'break' to try to prevent possible recursion issues.
        elif change_position.upper() == 'W': # West uphill
            Death()  # adventurer dies
        else:
            ClearFunction()


def EastDownhillHard():
    change_position = None
    while change_position not in list('nsNS'):  # require correct user input
        ClearFunction()
        print('As you wander down the hill, you notice a meadow appear as the sun comes out.')
        print('A flock of ravens appear to be knocking around here.')
        print('Perhaps this is their day job...')
        print()
        print('To head North where the ravens can watch you closely, enter: N')
        print('To head South towards an odd smell, enter: S')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'N':
            ClearFunction()
            print('This path seems to lead somewhere oddly familiar...')
            time.sleep(1)
            print('-' * os.get_terminal_size().columns)
            StartValleyHard()
            break  #  This is a cautionary 'break' to try to prevent possible recursion issues.
        elif change_position.upper() == 'S':
            ClearFunction()
            Winner()


def SouthMountainHard():
    change_position = None
    while change_position not in list('ewEW'):  # require correct user input
        ClearFunction()
        print('You find yourself upon the southern mountain.')
        print('The clouds up here are moving oddly slowly... and the sky has a golden aura!')
        print()
        print('To head West along the sourthern mountain ridge, enter: W')
        print('To head East along the sourthern mountain ridge, enter: E')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'W':
            ClearFunction()
            print('This path seems to lead somewhere oddly familiar...')
            time.sleep(1)
            print('-' * os.get_terminal_size().columns)
            StartValleyHard()
            break  #  This is a cautionary 'break' to try to prevent possible recursion issues.
        elif change_position.upper() == 'E':
            ClearFunction()
            Winner()


def WestUphillHard():
    change_position = None
    while change_position not in list('nsNS'):  # require correct user input
        ClearFunction()
        print('After wandering around for a while, you find a dark cave that compells you to enter.')
        print('You enter the cave and cannot find your way back out.')
        print('You come to hear a body of water ahead and somwhere it is rushing dangerously...')
        print()
        print('To head what seems to be North in the dark cave, enter: N')
        print('To head what seems to be South in the dark cave, enter: S')
        print()
        change_position = input(' >>> ').upper()
        if change_position.upper() == 'N':
            Death()  # adventurer dies
        elif change_position.upper() == 'S':
            ClearFunction()
            print('This path seems to lead somewhere oddly familiar...') # back to Start Valley
            time.sleep(1)
            print('-' * os.get_terminal_size().columns)
            StartValleyHard()
            break  #  This is a cautionary 'break' to try to prevent possible recursion issues.










def main():
    ## This is the creation of a class, in which to store information 
    ##   about the current player.
    ## I don't like objects, but in a game it seems best to use them.
    ## This is inside the 'main()' function so it resets every time the function runs.
    global current_player
    class current_player:
        score = 0  # this attribute of the object will track the score of the player
        name = ''  # this attribute of the object will hold the player's entered name
        mode = ''  # this attribute of the object will hold the player's chosen difficulty mode
        item = ''  # this attribute of the object will hold the item carried by the player


    ## Log the score to this file name; set filename as a variable
    ## This is inside the main() function to be pedantically certain it
    ##  is what it should be, before running the rest of the code which
    ##  uses it.
    global scorekeeper_log
    scorekeeper_log = 'lsd-scores.log'


    ## Run the menu.
    ClearFunction()
    Menu()
    input('< press enter to continue... >\n')  # pause for the user to press enter and carry on


    ## Start the game based on chosen mode.
    ClearFunction()
    if current_player.mode == 'E':
        StartValleyEasy()
    elif current_player.mode == 'M':
        StartValleyMedium() 
    elif current_player.mode == 'H':
        StartValleyHard() 
    else:
        #  Tell the user there has been an error that is fatal to the running of the program.
        #    (inform them it is an error related to difficulty 'mode'; then exit the program.)
        print('FATAL ERROR - mode error')
        exit()






#  Initialisation of the main function to start the program.
if __name__ == '__main__':
    main()
