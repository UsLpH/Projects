#random_string_gen.py :copyright: 2022 by UsLpH is licensed under CC BY-NC-SA 4.0
#https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1

from genericpath import exists
import random
from os import system
system("title UsLpH's random string generator")
import string
from time import time, sleep
while True:
    system("cls")
    print("length of strings : ", end="")
    le = input()
    print("number of strings to generate : ", end="")
    re = input()
    startTime = time()
    low = string.ascii_lowercase
    up = string.ascii_uppercase
    rand = ""
    rand2 = ""
    letters = string.ascii_letters
    nums = string.digits
    misc = string.punctuation
    yes = exists("UsLpH, " + re + " random strings.txt")
    no = random.choice(nums + letters + up + low) + random.choice(nums + letters + up + low) + random.choice(nums + letters + up + low) + random.choice(nums + letters + up + low)
    for i in range(int(re)):
        rand = (''.join(random.choice(nums + letters + up + low + "_") for i in range(int(le))))
        print (rand)
        rand = rand + "\n"
        rand2 = rand2 + rand

    if (yes == False):
            f = open("UsLpH, " + re + " random strings.txt", "a")
            f.write(rand2 + "\n")
            f.close()
    else:
            f = open("UsLpH, " + re + " random strings " + no + ".txt", "a")
            f.write(rand2 + "\n")
            f.close()
    
    executionTime = (time() - startTime)
    print('It took ' + str(executionTime) + " seconds to generate")
    sleep(3)