import random
import math

# definitive quitting 'screen'
def quit() : 
    print("===================================================================================================================\n")
    print("Thank you for playing!\n")
    print("===================================================================================================================\n")
    exit()

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
            if choice < 0 or choice > 5:
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
    print("After every turn, the computer will tell you whether your guess was too high, too low, or correct.")
    print("If you guess correctly, the computer will tell you a fun fact.\n\nGood luck!\n")

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
            print("Here is your fun fact: ")
            funFacts()
            print('')
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

def guessTheSuit() :
    print("\n===================================================================================================================\n")    

    print("INSTRUCTIONS: The computer will choose a card suit (Hearts, Spades, Diamonds, Clubs).")
    print("If you guess the correct suit, the computer will tell you a fun fact.\n\nGood luck!\n")

    print("===================================================================================================================\n")

    # pseudo-randomly selects a number between 1 and 100 -> for choosing 1/4 suits
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

    class InvalidEntry(Exception):
        "Raised when the guess is not one of the four card suits"
        pass

    # input a suit
    while True:
        try:
            guess = str(input("Enter your guess: "))
            guess = guess.lower()
            if ('hearts' not in guess) and ('spades' not in guess) and ('diamonds' not in guess) and ('clubs' not in guess):
                raise InvalidEntry
            break
        except ValueError:
            print("Please enter a valid suit...\n")    
            continue
        except InvalidEntry:
            print("Please enter a valid suit...\n")    
            continue

    if (guess != str(CPUanswer)):
        print("Better luck next time. The suit was "+ str(CPUanswer) + ".\n")
        while (playing != 'y' or playing != 'Y' or playing != 'n' or playing != 'N') :
            playing = input("Play again? (Y) Return to the Mini Game Room? (N): ")
            if (playing == 'y' or playing == 'Y') : guessTheSuit()
            elif (playing == 'n' or playing == 'N') : gameOptions()
    else: 
        print("Wow you guessed the suit!\n")
        print("Here is your fun fact: ")
        funFacts()
        print('')
        while (playing != 'y' or playing != 'Y' or playing != 'n' or playing != 'N') :
            playing = input("Play again? (Y) Return to the Mini Game Room? (N): ")
            if (playing == 'y' or playing == 'Y') : guessTheSuit()
            elif (playing == 'n' or playing == 'N') : gameOptions()

def highLow():
    print("\n===================================================================================================================\n")    

    print("INSTRUCTIONS: The computer will choose a number between 1-9. You must guess if the next card will be higher or lower.")
    print("If you guess correctly, the computer will tell you a fun fact.\n\nGood luck!\n")

    print("===================================================================================================================\n")

    # pseudo-randomly selects a number between 1 and 100 -> for choosing between 1 - 9
    CPUnumber1 = math.floor(random.random() * 100)
    CPUnumber1 = (CPUnumber1 % 9) + 1
    CPUanswer = 'equal'

    playing = ''

    print("... The Computer has chosen a number... "+ str(CPUnumber1) + "!\n")
    
    class InvalidEntry(Exception):
        "Raised when the guess is not 'higher' or 'lower"
        pass
    
    while True:
        try:
            guess = str(input("Please guess if the next number will be higher or lower than "+ str(CPUnumber1) + ": "))
            guess = guess.lower()
            if ('higher' not in guess) and ('lower' not in guess):
                raise InvalidEntry
            break
        
        except ValueError:
            print("Please enter 'higher' or 'lower'...\n")    
            continue
        
        except InvalidEntry:
            print("Please enter 'higher' or 'lower'...\n")    
            continue
        
    # CPUnumber2 cannot equal CPUnumber1 so it gets changed
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
        print("Here is your fun fact: ")
        funFacts()
        print('')
        while (playing != 'y' or playing != 'Y' or playing != 'n' or playing != 'N') :
            playing = input("Play again? (Y) Return to the Mini Game Room? (N): ")
            if (playing == 'y' or playing == 'Y') : highLow()
            elif (playing == 'n' or playing == 'N') : gameOptions()

def RPS():
    
    print("\n===================================================================================================================\n")    

    print("INSTRUCTIONS: The computer will choose rock, paper, or scissors. You must choose the option that will beat the computer.")
    print("Rock beats Scissors. Scissors beats Paper. Paper beats Rock.")
    print("If you win, the computer will tell you a fun fact.\n\nGood luck!\n")

    print("===================================================================================================================\n")

    # pseudo-randomly selects a number between 1 and 100 -> for choosing between 3 options
    CPUrandom = math.floor(random.random() * 100)
    CPUrandom = (CPUrandom % 3)
    CPUhand = 'none'

    playing = ''

    if (CPUrandom == 0):
        CPUhand = 'rock'
    elif (CPUrandom == 1):
        CPUhand = 'paper'
    else:
        CPUhand = 'scissors'

    print("...The Computer has chosen a suit...\n")

    print("Please select from the following choices:\n")
    print("- Rock")
    print("- Paper")
    print("- Scissors\n")

    class InvalidEntry(Exception):
        "Raised when the choice is not one of the three options."
        pass

    # input a hand
    while True:
        try:
            choice = str(input("Enter your choice: "))
            choice = choice.lower()
            if ('rock' not in choice) and ('paper' not in choice) and ('scissors' not in choice):
                raise InvalidEntry
            break
        except ValueError:
            print("Please enter a valid hand...\n")    
            continue
        except InvalidEntry:
            print("Please enter a valid hand...\n")    
            continue

    # if CPU beats player
    if (choice == 'rock' and CPUhand == 'scissors') or (choice == 'scissors' and CPUhand == 'paper') or (choice == 'paper' and CPUhand == 'rock'):
        print("Better luck next time. The computer chose "+ str(CPUhand) + " which beats your "+ choice + ".\n")
        while (playing != 'y' or playing != 'Y' or playing != 'n' or playing != 'N') :
            playing = input("Play again? (Y) Return to the Mini Game Room? (N): ")
            if (playing == 'y' or playing == 'Y') : RPS()
            elif (playing == 'n' or playing == 'N') : gameOptions()
    # if there's a draw
    elif (choice == CPUhand):
        print("You both chose "+ CPUhand+ "! No winner this round.")
        while (playing != 'y' or playing != 'Y' or playing != 'n' or playing != 'N') :
            playing = input("Play again? (Y) Return to the Mini Game Room? (N): ")
            if (playing == 'y' or playing == 'Y') : RPS()
            elif (playing == 'n' or playing == 'N') : gameOptions()
    # if player beats CPU
    else: 
        print("Wow you won! You chose "+ choice + " which beats the computer's "+ CPUhand + ".\n")
        print("Here is your fun fact: ")
        funFacts()
        print('')
        while (playing != 'y' or playing != 'Y' or playing != 'n' or playing != 'N') :
            playing = input("Play again? (Y) Return to the Mini Game Room? (N): ")
            if (playing == 'y' or playing == 'Y') : RPS()
            elif (playing == 'n' or playing == 'N') : gameOptions()

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
        print("Clouds weigh up to 1 million pounds or MORE.")
    elif (factNum == 6):
        print("20% of all the oxygen you breathe is used by your brain.")
    elif (factNum == 7):
        print("Tiger shark embryos begin attacking each other in their mother's womb before they are even born.")
    elif (factNum == 8):
        print("The Nobel Peace Prize is named for Alfred Nobel, the inventor of dynamite.")
    elif (factNum == 9):
        print("If you have a fear of ducks watching you constantly, that is called 'anatidaephobia'. Quack quack.")
    elif (factNum == 10):
        print("German chocolate cake was invented in Texas in 1852 by a man named Sam German.")
    elif (factNum == 11):
        print("There are over 4 million vending machines around Japan, of which more than 2 million are for selling drinks.")
    elif (factNum == 12):
        print("The current American flag was designed by a high school student in 1958.")
    elif (factNum == 13):
        print("The # symbol isn't officially called hashtag or pound... It's called an octothorpe.")
    elif (factNum == 14):
        print("Cap'n Crunch's full name is Horatio Magellan Crunch.")
    elif (factNum == 15):
        print("The Ancient Romans used to drop a piece of toast into their wine for good health - hence why we 'raise a toast'.")
    elif (factNum == 16):
        print("The unicorn is the national animal of Scotland. The Welsh Dragon is the national animal of Wales!")
    elif (factNum == 17):
        print("The Japanese word 'Kuchi zamishi' is the act of eating when you're not hungry because your mouth is lonely.")
    elif (factNum == 18):
        print("One quarter of all your bones are located in your feet.")
    elif (factNum == 19):
        print("France executed the last person by guillotine as recently as the same year 'Star Wars: A New Hope' came out.")
    elif (factNum == 20):
        print("Cleopatra lived closer to the time Pizza Hut was founded than to when the Egyptian pyramids were built.")
    elif (factNum == 21):
        print("A day on Venus is longer than a year on Venus. It is also the only planet in our solar system to rotate clockwise!")
    elif (factNum == 22):
        print("Did you know sharks don't have bones? Instead, its skeleton is made of cartilage.")
    elif (factNum == 23):
        print("Despite their large size, whales seem unable to get cancer. (Check out Peto's Paradox to learn more)")
    else:
        print("It can take from 144 to 1000 licks to reach the tootsie roll center of a Tootsie Pop.")

title()
