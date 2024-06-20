name = input("Please type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can either go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river. You can [walk] around it or [swim] across. ").lower()
    if answer == "walk":
        print("You walked for many miles, ran out of food, and passed out from exhaustion. YOU LOSE.")
    elif answer == "swim":
        print("You swam across and were eaten by an alligator. YOU LOSE.")
    else: 
        print("Not a valid option. You stare at the river until the flow of time stops. YOU LOSE.")
elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Do you [cross] it or head [back]? ").lower()
    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? [yes/no] ").lower()
        if answer == "yes":
            print("You talk to the stranger and they show you how to escape this place. YOU WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended. You are turned into a lizard. YOU LOSE.")
        else: 
            print("Not a valid option. The stranger leaves you to fend for yourself. YOU LOSE.")
    elif answer == "back":
        print("You try to head back to the main road. The path is gone and you find yourself lost in this mysterious place. YOU LOSE.")
    else: 
        print("Not a valid option. You stare at the river until the flow of time stops. YOU LOSE.")
else:
    print("Not a valid option. You stand at the crossroads until the end of time. YOU LOSE.")

print("Thank you for playing, " + name + ". I hope you enjoyed!")