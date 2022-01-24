import random #import all the randomizing function stuff
import time #import time function stuff for delay
while 1:
    trigger = input("Do you want to flip a coin? (Y/N) ")
    while trigger != "Y" and trigger != "y" and trigger != "Yes" and trigger != "yes" and trigger != "yeah" and trigger != "Yeah": #create a loop which will ask the user if he wants to flip a coin until he types yes
        trigger = input("Do you want to flip a coin? (Y/N)")
    possibilities = ["Heads", "Tails"]
    print ("And the coin landed on....")
    time.sleep(2) #chil out for 2 seconds
    print (random.choice(possibilities)) #picking a random element out of the list possibilities