import random

print("WELCOME !!!!")
print("The Game is Set for You")

option = int(input("Choose one of the below\n 1.Rock , 2.Paper , 3.scissor\n"))
Computer = int(random.randint(1,3))


Rock =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper =("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


if option == 1:
    print(Rock)
    if Computer == 1:
        print("It's computer turn\n")
        print(Rock)
        print("The Result Draw")
    elif Computer == 2:
        print("It's computer turn\n")
        print(Paper)
        print("Oooo YOU LOOSE")
    elif Computer == 3:
        print("It's computer turn\n")
        print(scissors)
        print("Congratulations YOU WIN !!!")
elif option == 2:
    print(Paper)
    if Computer ==1:
        print("It's computer turn\n")
        print(Rock)
        print("Congratulations YOU WIN !!!")
    elif Computer == 2:
        print("It's computer turn\n")
        print(Paper)
        print("The Result Draw")
    elif Computer == 3:
        print("It's computer turn\n")
        print(scissors)
        print("Oooo YOU LOOSE")
elif option == 3:
    print(scissors)
    if Computer ==1:
        print("It's computer turn\n")
        print(Rock)
        print("Oooo YOU LOOSE")
    elif Computer == 2:
        print("It's computer turn\n")
        print(Paper)
        print("Congratulations YOU WIN !!!")
    elif Computer == 3:
        print("It's computer turn\n")
        print(scissors)
        print("The Result Draw")
else:
    print("You Choose Wrong")
