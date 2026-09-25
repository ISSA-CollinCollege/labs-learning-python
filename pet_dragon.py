# This is a pet dragon project that I came up with.
# The dragon will have a hunger valuse set 1 - 10.
# 10 food items will be present to feed the dragon. The food items will have values set 1 - 10.
# When the dragon is full he will say thank you and give you a lucky number.

import random

# Dragon looks wonky in the text editor, but prints correctly in the console. This is because the ASCII art has break out \\ that I don't want to replace so I just left them.
print("                 ___====-_  _-====___")
print("           _--^^^#####//      \\#####^^^--_")
print("       _-^##########// (    ) \\##########^-_")
print("       -############//  |\^^/|  \\############-")
print("     _/############//   (@::@)   \\\############\_")
print("    /#############((     /\/\     ))#############\\")
print("   -###############\\\    (oo)    //###############-")
print("  -#################\\\  / VV \  //#################-")
print(" -###################\\\/      \//###################-")
print("_#/|##########/\######(   /\   )######/\##########|\#_")
print("/ |#/\#/\#/\/  \#/\##\   |   |  /##/\#/  \/\#/\#/\#| \|")
print("`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '")
print("   `   `  `      `   / | |  | | \   '      '  '   '")
print("                    (  | |  | |  )")

print("                   __\ | |  | | /__")
print("                  (vvv(VVV)(VVV)vvv)")

# Assign dragon's hunger rating
dragon_hunger = random.randint(1,10)

# Function to let user know how hungry the dragon is
def feed_dragon(dragon_hunger):
    match dragon_hunger:
        case 1:
            return print("I'm not very hungry right now, but I should still eat...")
        case 2:
            return print("I'm a bit peckish.")
        case 3:
            return print("Maybe a little snack will fill me up.")
        case 4:
            return print("I'm starting to feel a bit more hungry.")
        case 5:
            return print("Food is starting to sound very good right now.")
        case 6:
            return print("I think it is getting close to my lunch time.")
        case 7:
            return print("My stomach is beginning to growl.")
        case 8:
            return print("I could really use a good meal right now")
        case 9:
            return print("I could eat a cow!")
        case 10:
            return print("I am absolutely starving right now! FEED ME!")

feed_dragon(dragon_hunger)

# User decides what to feed dragon
food = int(input("What should you feed him?\n 1. Carrot \n 2. Salad \n 3. Beef Jerky \n 4. Ramen Noodles \n 5. Pizza \n 6. Hamburger \n 7. Spaghetti \n 8. Steak \n 9. A Cow \n 10. Everything in the kitchen! \n"))
if food == dragon_hunger:
    print(f"That was exactly what I needed! Thank you. Your lucky number is {random.randint(1,100)}")
elif food < dragon_hunger:
    print("That wasn't very satisfying. Maybe try harder next time.")
elif food > dragon_hunger:
    print("Whoa! That was way too much food! Next time not so much...")
    
