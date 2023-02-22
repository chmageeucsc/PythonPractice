import random
import math

# definitive quitting 'screen'
def quit() : 
    print("===================================================================================================================\n")
    print("Thank you for playing!\n")
    print("===================================================================================================================\n")

# special word art for title 'screen'
def title() :
    print(" __  __     _               _               ___                                      ___                           ")
    print("|  \/  |   (_)    _ _      (_)      o O O  / __|   __ _    _ __     ___      o O O  | _ \    ___     ___    _ __   ")
    print("| |\/| |   | |   | ' \     | |     o      | (_ |  / _` |  | '  \   / -_)    o       |   /   / _ \   / _ \  | '  \  ")
    print("|_|__|_|  _|_|_  |_||_|   _|_|_   TS__[O]  \___|  \__,_|  |_|_|_|  \___|   TS__[O]  |_|_\   \___/   \___/  |_|_|_| ")
    print("_|'''''|_|'''''|_|'''''|_|'''''| {======|_|'''''|_|'''''|_|'''''|_|'''''| {======|_|'''''|_|'''''|_|'''''|_|'''''| ")
    print("''-0-0-'''-0-0-'''-0-0-'''-0-0-'./o--000'''-0-0-'''-0-0-'''-0-0-'''-0-0-'./o--000'''-0-0-'''-0-0-'''-0-0-'''-0-0-' ")
    print("===================================================================================================================\n")

    print("Welcome to the Mini Game Room! Feel free to play as long as you want.\n")

    print("===================================================================================================================\n")

    gameOptions()

# prints game options
def gameOptions() :
    print("[1] Guess the Number")
    print("[2] Guess the Suit")
    print("[3] High Card, Low Card")
    print("[4] Rock, Paper, Scissors")
    print("[5] Mad Libs")
    print("\n[0] Leave Mini Game Room")

    print("\n===================================================================================================================\n")
    # define Python user-defined exceptions
    class InvalidEntry(Exception):
        "Raised when there are more than 3 inputs"
        pass

    # input a number
    while True:
        try:
            choice = int(input("Input the number of the game you would like to play: "))
            print('')
            if choice < 0 or choice > 4:
                raise InvalidEntry
            break
        except ValueError:
            print("Please enter a whole number...")  
            continue
        except InvalidEntry:
            print("Please choose from one of the options.\n")  
            continue

    if choice == 1:
        print("[1] Guess the Number")
        guessTheNumber()

    if choice == 2:
        print("[2] Guess the Suit")
        guessTheSuit()

    if choice == 3:
        print("[3] High Card, Low Card")
        highLow()

    if choice == 4: 
        print("[4] Rock, Paper, Scissors")
        RPS()

    if choice == 5:
        print("[5] Mad Libs")
        madLibs()

    if choice == 0: quit()

def guessTheNumber() :
    print("\n===================================================================================================================\n")    

    print("INSTRUCTIONS: The computer will choose a number between 1 - 100. You will try to guess the number within 7 turns.")
    print("After every turn, the computer will tell you whether your guess was too high, too low, or correct.\n\nGood luck!\n")

    print("===================================================================================================================\n")

    # pseudo-randomly selects a number between 1 and 100
    CPUnumber = math.floor(random.random() * 100)

    numGuesses = 7

    playing = ''

    print("...The Computer has chosen a number...\n")

    # define Python user-defined exceptions
    class InvalidEntry(Exception):
        "Raised when the guess is not between 1 - 100"
        pass

    # input a number
    while True:
        try:
            guess = int(input("Enter your guess: "))
            numGuesses -= 1
            if guess < 1 or guess > 100:
                raise InvalidEntry
            break
        except ValueError:
            print("Please enter a number...\n")    
            continue
        except InvalidEntry:
            print("Please choose between 1 - 100...\n") 
            continue

    # the player has 7 tries to guess the correct number
    while (numGuesses > 0):
        # if the player's guess is greater than the CPU number
        if (guess > CPUnumber):
            print("Your guess was higher than the number.")
            print("You have " + str(numGuesses) + " guess(es) left.")
            try:
                guess = int(input("Enter your guess: "))
                numGuesses -= 1
                if guess < 1 or guess > 100:
                    raise InvalidEntry
                continue
            except ValueError:
                print("Please enter a number...\n")    
                continue
            except InvalidEntry:
                print("Please choose between 1 - 100...\n") 
                continue
        # if the player's guess is less than the CPU number
        elif (guess < CPUnumber):
            print("Your guess was lower than the number.")
            print("You have " + str(numGuesses) + " guess(es) left.")
            try:
                guess = int(input("Enter your guess: "))
                numGuesses -= 1
                if guess < 1 or guess > 100:
                    raise InvalidEntry
                continue
            except ValueError:
                print("Please enter a number...\n")    
                continue
            except InvalidEntry:
                print("Please choose between 1 - 100...\n") 
                continue
        # if the player guesses correctly
        else:
            print("Wow you guessed the number!\n")
            while (playing != 'y' or playing != 'Y' or playing != 'n' or playing != 'N') :
                playing = input("Play again? (Y) Return to the Mini Game Room? (N): ")
                if (playing == 'y' or playing == 'Y') : guessTheNumber()
                elif (playing == 'n' or playing == 'N') : gameOptions()

    # if the player cannot guess in 7 tries, ask to play again or go to main menu
    if (numGuesses == 0):
        print("Better luck next time! The number was "+ str(CPUnumber) + ".\n")
        while (playing != 'y' or playing != 'Y' or playing != 'n' or playing != 'N') :
            playing = input("Play again? (Y) Return to the Mini Game Room? (N): ")
            if (playing == 'y' or playing == 'Y') : guessTheNumber()
            elif (playing == 'n' or playing == 'N') : gameOptions()

# add fun facts code
def guessTheSuit() :
    print("\n===================================================================================================================\n")    

    print("INSTRUCTIONS: The computer will choose a card suit (Hearts, Spades, Diamonds, Clubs).")
    print("If you guess the correct suit, the computer will tell you a fun fact.\n\nGood luck!\n")

    print("===================================================================================================================\n")

    CPUnumber = math.floor(random.random() * 100)
    CPUnumber = (CPUnumber % 4) + 1
    CPUanswer = 'none'

    playing = ''

    if(CPUnumber == 1):
        CPUanswer = 'hearts'
    if(CPUnumber == 2):
        CPUanswer = 'spades'
    if(CPUnumber == 3):
        CPUanswer = 'diamonds'
    if(CPUnumber == 4):
        CPUanswer = 'clubs'

    print("...The Computer has chosen a suit...\n")

    print("Please select from the following choices:\n")
    print("- Hearts")
    print("- Spades")
    print("- Diamonds")
    print("- Clubs")

    # input a number
    while True:
        try:
            guess = str(input("Enter your guess: "))
            guess.lower()
            break
        except ValueError:
            print("Please enter a suit...\n")    
            continue

    if (guess != str(CPUanswer)):
        print("Better luck next time. The suit was "+ str(CPUanswer) + ".\n")
        while (playing != 'y' or playing != 'Y' or playing != 'n' or playing != 'N') :
            playing = input("Play again? (Y) Return to the Mini Game Room? (N): ")
            if (playing == 'y' or playing == 'Y') : guessTheSuit()
            elif (playing == 'n' or playing == 'N') : gameOptions()
    else: 
        print("Wow you guessed the suit!\n")
        while (playing != 'y' or playing != 'Y' or playing != 'n' or playing != 'N') :
            playing = input("Play again? (Y) Return to the Mini Game Room? (N): ")
            if (playing == 'y' or playing == 'Y') : guessTheSuit()
            elif (playing == 'n' or playing == 'N') : gameOptions()

# add fun facts code
def highLow():
    print("\n===================================================================================================================\n")    

    print("INSTRUCTIONS: The computer will choose a number between 1-9. You must guess if the next card will be higher or lower.")
    print("If you guess correctly, the computer will tell you a fun fact.\n\nGood luck!\n")

    print("===================================================================================================================\n")

    CPUnumber1 = math.floor(random.random() * 100)
    CPUnumber1 = (CPUnumber1 % 9) + 1
    CPUanswer = 'equal'

    playing = ''

    print("... The Computer has chosen a number... "+ str(CPUnumber1) + "!\n")

    """
    class InvalidEntry(Exception):
        "Raised when the guess is not between 1 - 100"
        pass
    """
    
    while True:
        try:
            guess = str(input("Please guess if the next number will be higher or lower than "+ str(CPUnumber1) + ": "))
            guess.lower()
            break
            # fix input to only take 'higher' or 'lower'
            """
            if (guess != 'higher'or guess != 'lower'):
                raise InvalidEntry
            break
        """
        except ValueError:
            print("Please enter 'higher' or 'lower'...\n")    
            continue
        """
        except InvalidEntry:
            print("Please enter 'higher' or 'lower'...\n")    
            continue
        """

    CPUnumber2 = CPUnumber1
    while (CPUnumber2 == CPUnumber1):
        CPUnumber2 = math.floor(random.random() * 100)
        CPUnumber2 = (CPUnumber2 % 9) + 1

    if (CPUnumber2 < CPUnumber1):
        CPUanswer = 'lower'
    else:
        CPUanswer = 'higher'

    if (guess != str(CPUanswer)):
        print("Better luck next time. The number was "+ str(CPUnumber2) + ".\n")
        while (playing != 'y' or playing != 'Y' or playing != 'n' or playing != 'N') :
            playing = input("Play again? (Y) Return to the Mini Game Room? (N): ")
            if (playing == 'y' or playing == 'Y') : highLow()
            elif (playing == 'n' or playing == 'N') : gameOptions()
    else: 
        print("Wow you guessed correctly! The number was "+ str(CPUnumber2) + ".\n")
        while (playing != 'y' or playing != 'Y' or playing != 'n' or playing != 'N') :
            playing = input("Play again? (Y) Return to the Mini Game Room? (N): ")
            if (playing == 'y' or playing == 'Y') : highLow()
            elif (playing == 'n' or playing == 'N') : gameOptions()

def RPS():
    print("Rock, Paper, Scissors")
    CPUrandom = math.floor(random.random() * 100)
    CPUrandom = (CPUrandom % 3)

    if (CPUrandom == 0):
        print("rock")
    elif (CPUrandom == 1):
        print("paper")
    else:
        print("scissors")

def madLibs():
    print("MadLibs")

def funFacts():
    factNum = math.floor(random.random() * 100)
    factNum = (factNum % 25)
    if (factNum == 0):
        print("There are more trees on Earth than there are stars in the Milky Way(3 trillion trees vs 100-400 billion stars).")
    elif (factNum == 1):
        print("It can rain diamonds on Nepture, Uranus, and Saturn.")
    elif (factNum == 2):
        print("There is enough DNA in the average person's body to stretch from the sun to Pluto and back — 17 times!")
    elif (factNum == 3):
        print("In an entire lifetime, the average person walks the equivalent of five times around the world.")
    elif (factNum == 4):
        print("Hot water freezes faster than cold water... Seriously. Feel free to look it up.")
    elif (factNum == 5):
        print("fun")
    elif (factNum == 6):
        print("fun")
    elif (factNum == 7):
        print("fun")
    elif (factNum == 8):
        print("fun")
    elif (factNum == 9):
        print("fun")
    elif (factNum == 10):
        print("fun")
    elif (factNum == 11):
        print("fun")
    elif (factNum == 12):
        print("fun")
    elif (factNum == 13):
        print("fun")
    elif (factNum == 14):
        print("fun")
    elif (factNum == 15):
        print("fun")
    elif (factNum == 16):
        print("fun")
    elif (factNum == 17):
        print("fun")
    elif (factNum == 18):
        print("fun")
    elif (factNum == 19):
        print("fun")
    elif (factNum == 20):
        print("fun")
    elif (factNum == 21):
        print("fun")
    elif (factNum == 22):
        print("fun")
    elif (factNum == 23):
        print("fun")
    else:
        print("fun")

title()
