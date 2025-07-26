import random

letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
number = ["0","1","2","3","4","5","6","7","8","9"]
symbol = ["!","@","#","$","%","&","*"]

print("WELCOME TO PASSWARD GENERATOR")
nu_letter = int(input("Enter How many letter you want to in your passward\n"))
nu_number = int(input("Enter How many number you want to in your passward\n"))
nu_symbol = int(input("Enter How many symbol you want to in your passward\n"))

passwards = []

for lett in range(0,nu_letter):
    passwards.append(random.choice(letter))

for num in range(0,nu_number):
    passwards.append(random.choice(number))

for sym in range(0,nu_symbol):
    passwards.append(random.choice(symbol))


random.shuffle(passwards)
print("Your Passwrd is")
print("".join(passwards))
