#symmetric_file_encryptor.py © 2022 by UsLpH is licensed under CC BY-NC-SA 4.0
#https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1


from operator import length_hint
from time import sleep, time
from os.path import exists
from os import system
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
system("title Symmetric Encryptor")

if (exists("IV") == False):
    while True:
        print("Enter Initialization Vector (16 character key) : ", end="")
        IV = input()
        if len(IV) != 16:
            print("IV must be 16 characters long")
            print (len(IV))
            sleep(3)
            system("cls")
        else:    
            open("IV", "a").write(IV)
            break
else:
    IV = open("IV", "r").read()
    IV = str.encode(IV)

while True:
    system("cls")
    print("Enter Key To Encrypt File With (16 or 32 character key) : ", end="")
    ogKeykey = input()
    system("cls")
    if (len(ogKeykey) != 16 and len(ogKeykey) != 32):
        system("cls")
        print("Invalid Key Length")
        print (len(ogKeykey))
        sleep(3)
    else:
        break

while True:

    key = ogKeykey.encode('UTF-8')
    cipher = Cipher(algorithms.AES(key), modes.GCM(IV))
    encryptor = cipher.encryptor()
    decryptor = cipher.decryptor()

    print("Current Key : " + ogKeykey)
    print("Drag File and press enter")
    fiile = input()
    startTime = time()
    with open(fiile, 'rb') as file:
        original = file.read()
    encrypted = encryptor.update(original) + encryptor.finalize()
    with open(fiile, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    

    executionTime = (time() - startTime)
    print('It took ' + str(executionTime) + " seconds to encrypt / decrypt")
    sleep(1)
    system("cls") 