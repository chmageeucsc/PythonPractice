# input anything
while True:
  try:
    choice = input("Enter anything: ")
    break
  except ValueError:
      print("Please enter something...")  
      continue

choice = len(choice) % 4

print("\nYou chose option "+ str(choice) + ".\n")

if choice == 0: 
    mission_name = input("Enter your name: ")
    mission_verb1 = input("Enter a verb: ")
    mission_adj1 = input("Enter an adjective: ")
    mission_funkyWord = input("Enter a silly word: ")    
    mission_num = input("Enter a number: ")     
    mission_noun1 = input("Enter a noun: ")  
    mission_adj2 = input("Enter another adjective: ")  
    mission_noun2 = input("Enter another noun: ")    
    mission_occupation = input("Enter an occupation: ")     
    mission_time = input("Enter an amount of time: ")    
    mission_verb2 = input("Enter another verb: ")       
    mission_location = input("Enter a location: ")   
    mission_verb3 = input("Enter a verb ending in '-ed': ")  
    mission_noun3 = input("Enter a plural noun: ")
    mission_adj3 = input("Enter another adjective: ")
    mission_verb4 = input("Enter a verb ending in '-ing': ")
    mission_verb5 = input("Enter another verb: ")
    
    print("\nGood morning, " + mission_name + ".\n")
    print("Your mission, should you choose to "+ mission_verb1 +
            " it, involves the recovery of a "+ mission_adj1 + " item designated '"+ mission_funkyWord + "'.\n")
    print("You may select any "+ mission_num + " "+ mission_noun1 + " members, but it is "+ mission_adj2 + 
            " that the third member of your "+ mission_noun1 + " be Nyah Nordoff-Hall. She is a "+ mission_noun2 +
            ", and a highly capable professional "+ mission_occupation + 
            ". You have "+ mission_time + " to "+ mission_verb2 + " Miss Hall and meet me in "+ mission_location + 
            " to receive your assignment.\n")
    print("As always, should any member of your "+ mission_noun1 + " be caught or "+ mission_verb3 + 
            ", the Secretary will disavow all knowledge of your "+ mission_noun3 + 
            ". And Mr. Hunt, the next time you go on holiday, please be "+ mission_adj3 + 
            " enough to let us know where you`re "+ mission_verb4 + ".\n")
    print("This message will self-"+ mission_verb5 + " in five seconds.\n\nBoom.\n")

if choice == 1: 
    twelfth_holiday = input("Enter a holiday: ")
    twelfth_adj1 = input("Enter an adjective: ")
    twelfth_occ1 = input("Enter a plural occupation: ")
    twelfth_verb1 = input("Enter a verb ending in '-ing': ")
    twelfth_verb2 = input("Enter another verb ending in '-ing': ")
    twelfth_noun1 = input("Enter a plural noun: ")
    twelfth_noun2 = input("Enter another plural noun: ")
    twelfth_occ2 = input("Enter another plural occupation: ")
    twelfth_verb3 = input("Enter another verb ending in '-ing': ")
    twelfth_noun3 = input("Enter another plural noun: ")
    twelfth_adj2 = input("Enter another adjective: ")
    twelfth_verb4 = input("Enter another verb ending in '-ing': ")
    twelfth_nationality = input("Enter a nationality: ")
    twelfth_noun4 = input("Enter another plural noun: ")
    twelfth_animal = input("Enter an animal: ")
    twelfth_food = input("Enter a food: ")

    print("\nOn the twelfth day of "+ twelfth_holiday + ", my "+ twelfth_adj1 + 
    " love sent to me \n\nTwelve "+ twelfth_occ1 + " "+ twelfth_verb1 + 
    ", \nEleven pipers "+ twelfth_verb2 + ", \nTen "+ twelfth_noun1 + 
    " a leaping, \nNine "+ twelfth_noun2 + " dancing, \nEight "+ twelfth_occ2 + 
    " a milking, \nSeven swans a "+ twelfth_verb3 + ", \nSix "+ twelfth_noun3 + 
    " a laying, \nFive "+ twelfth_adj2 + " rings, \nFour "+ twelfth_verb4 + 
    " birds, \nThree "+ twelfth_nationality + " Hens, \nTwo turtle "+ twelfth_noun4 + 
    ", \nAnd a/an "+ twelfth_animal + " in a/an "+ twelfth_food + 
    " tree.\n\nHappy "+ twelfth_holiday + "!\n")

if choice == 2: 
    day_verb1 = input("Enter a verb ending in '-ing': ")
    day_verb2 = input("Enter another verb ending in '-ing': ")
    day_verb3 = input("Enter a verb ending in '-ed': ")
    day_adj1 = input("Enter an adjective: ")
    day_adj2 = input("Enter another adjective: ")
    day_adv = input("Enter an adverb: ")
    day_place = input("Enter a place: ")
    day_verb4 = input("Enter a verb: ")
    day_verb5 = input("Enter another verb: ")

    print("\nTommorrow is a new day full of new suprises and new adventures. Such as "+ day_verb1 + 
    " and "+ day_verb2 + ". \nTommorrow leads you to the life you haven`t "+ day_verb3 + 
    " yet. So why not plan to live today with the most "+ day_adj1 + " and "+ day_adj2 + 
    " outlook. \nBecause today is yesterday`s tommorrow and we all know that it`s good to do things "+ day_adv + 
    ". \nSo let`s go to "+ day_place + " and "+ day_verb4 + " with someone cool. Or you could just let it "+ day_verb5 + " right by.\n")

if choice == 3:
    alien_noun1 = input("Enter a plural noun: ")
    alien_occupation = input("Enter an occupation: ")
    alien_animal = input("Enter an animal: ")
    alien_place = input("Enter a place: ")
    alien_verb1 = input("Enter a verb: ")
    alien_verb2 = input("Enter a verb ending in '-ed': ")
    alien_noun2 = input("Enter another noun: ")

    print("\nIn the book War of the "+ alien_noun1 + ", the main character is an anonymous "+ alien_occupation + 
        " who records the arrival of "+ alien_animal +" in "+ alien_place+ ". Needless to say, havoc reigns as the "+ alien_animal + 
        " continue to "+ alien_verb1 + " everything in sight, until they are "+ alien_verb2 + " by the common "+ alien_noun2 +".\n")