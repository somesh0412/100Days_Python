print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("WELCOME TO TREASURE ISLAND !!!")
print("Your Mission is to find the trasure")
print("You're at a cross road. Where do you want to go ?")

Dir = str(input("Type left OR right\n")).lower()
if Dir == 'left':
    print("You've outsmarted the island's challenges! ")
    Choose_Situation = str(input("You are near the River choose the situation \n Type Swim Or Wait\n")).lower()
    if Choose_Situation == 'wait':
        print("You've proven yourself a worthy adventurer!")
    
        Choose_Door = str(input("You are in last step Choose one Door Color \n type Red,Yellow,Blue\n")).lower()
        if Choose_Door == 'red':
            print("You are burn in fire.\nBetter luck next time, adventurer! \n GAME OVER!!!")
        elif Choose_Door == 'blue':
            print("You fall from hight\n The treasure remains hidden... for now.\nGAME OVER!!!")
        else:
            print("Congratulations, you've found the treasure!!!")
    else:
        print("The animal is attack on You.\nThe island claims another victim... \n GAME OVER!!!")
else:
    print("You fall in hole.\nYour quest has ended in defeat. \n GAME OVER!!!")









