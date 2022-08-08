import random;
import os;
import time;
import termcolor;

os.system("cls")
#Intro
file = open("rules.txt")
logo = termcolor.colored(file.read(),"yellow")
i=15
while (i!=0):
    i=i-1
    print(logo)
    print(f"The game will start in {i+1}")
    time.sleep(1)
    os.system("cls")

tries = 0

#DEF
min = int(input("Minimum ="))
max = int(input("Maximum ="))

if (max <= min):
    print(f"Enter a number higher than {min}")
else:
    os.system("cls")
    print("Loading game.")
    time.sleep(1)
    os.system("cls")
    print("Loading game..")
    time.sleep(1)
    os.system("cls")
    print("Loading game...")
    time.sleep(1)
    Answer = random.randint(min+1,max-1)
    GAME = True

while(GAME):
    os.system("cls")
    print(f"Minimum = {min} | Maximum = {max}")
    query = input("Answer = ")
    tries += 1

    if(query.isnumeric() == False):
        print("This is not a valid number !")
        time.sleep(2)
    else:
        query = int(query)
        if (query > min and query < Answer):
            min = query;
        if (query < max and query > Answer):
            max = query;
        if (query == Answer):
            print("!! You won !!")
            print("\n\n\nThere is some stats :")
            print(f"The secret number was {query}, and you took {tries} try !")
            print("the game will stop soon")
            time.sleep(5)
            GAME = False
            os.system("cls")

            
