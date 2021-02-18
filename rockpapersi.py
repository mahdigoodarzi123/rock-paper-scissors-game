# importing part
import random

print("hello and welcome to my game :)")
print("help:r is for rock , s is for Scissors , p is for paper")
print("------------------------------")
#inputin palyer answer
palyer = input("please choose your tool: ")
print("player 1: ", palyer)
print("------------------------------")


#random number choosing part
randomnumber = random.randint(0,2)
if randomnumber == 0:
    print("computer: r")
elif randomnumber == 1:
    print("computer: p")
elif randomnumber == 2:
    print("computer: s")


#a while loop
while True:

    if palyer == "rock" :
        randomnumber = random.randint(0,2)

        if randomnumber == 0:
            print("computer: r")
        elif randomnumber == 1:
            print("computer: p")
        elif randomnumber == 2:
            print("computer: s")
    elif palyer == "Scissors":
        randomnumber = random.randint(0,2)
        if randomnumber == 0:
            print("computer: r")
        elif randomnumber == 1:
            print("computer: p")
        elif randomnumber == 2:
            print("computer: s")
    elif palyer == "kaghaz":
        randomnumber = random.randint(0,2)
        if randomnumber == 0:
            print("computer: r")
        elif randomnumber == 1:
            print("computer: p")
        elif randomnumber == 2:
            print("computer: s")



# who won the game part(judge!)
    #for r
    if (palyer == "r") and (randomnumber == 0):
        print("oops,try again!!")
        break
    if (palyer == "r") and (randomnumber == 1):
        print("sorry,you lost:((((")
        break
    if (palyer == "r") and (randomnumber == 2):
        print("congrats you won")
        break

    #for p
    if (palyer == "p") and (randomnumber == 0):
        print("sorry,you lost:((((")
        break
    if (palyer == "p") and (randomnumber == 1):
        print("oops,try again")
        break
    if (palyer == "p") and (randomnumber == 2):
        print("congrats you won")
        break

    #for s
    if (palyer == "s") and (randomnumber == 0):
        print("sorry,you lost:((((")
        break
    if (palyer == "s") and (randomnumber == 1):
        print("congrats you won")
        break
    if (palyer == "s") and (randomnumber == 2):
        print("oops,try again")
        break