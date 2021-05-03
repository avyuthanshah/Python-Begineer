import random
import os

print("Number Guessing Game")
print("\n Designed by Avyuthan ")

number = int(random.randrange(1, 51))


def valuestatus(difference,vall):

    if 1 <= difference < 3:
        print("Lava hot")
    elif 3 <= difference < 6:
        print("Boiling Hot")
    elif 6 <= difference < 12:
        print("Hot")
    elif 12 <= difference < 20:
        print("Kinda hot")
    elif 20 <= difference < 30:
        print("Moderate temp")
    elif 30 <= difference < 35:
        print("Getting cold")
    elif 35 <= difference < 40:
        print("Cold")
    elif 40 <= difference < 45:
        print("Ice Cold")
    elif 45 <= difference <= 50:
        print("Extreme Artic Cold")
    elif vall > 50:
        print("Invalid Input. Guess between 1-50 only")


value = 0
count = 0

while count != 10:
    value = int(input("Guess the number: "))
    diff = abs(value-number)
    valuestatus(diff, value)
    count += 1

    if value == number:
        print("Yeah you got the number in {} tries".format(count))
        break

if count==10:
    print("MAX GUESS REACHED")
    print("Num was {}".format(number))


os.system("Pause")
