from discord_webhook import DiscordWebhook # For webhook
import requests # for database 
from os import system as sys # for clearing screen and pausing
import getpass # for pc username 
import subprocess # for hwid
import hashlib # for encryption
from time import sleep # for sleep



webhook2 = "" #set webhook to send requests to

s = requests.get("") #get the data from the database

current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()#grab pc hwid



key = input() #get user input (text entered)

hash = hashlib.sha256((current_machine_id + key).encode()) #make new key encrypting the hwid and key together
sha = hash.hexdigest() #convert to text

hash2 = hashlib.sha256(key.encode()) #encrypt key alone
sha2 = hash2.hexdigest() #convert to text

if(sha2 in s.text): #if the key alone is in database

    webhook = DiscordWebhook(url=webhook2, content="Request : " + sha + " | " + getpass.getuser()) #set request with key +hwid and pc username
    response = webhook.execute() #send request

    sys("cls") #clear the screen
    print("Request Sent")
    sleep(5)
elif(sha in s.text): #if the key and hwid are in the database 
    sys("cls") #clear the screen
    print("Accepted")
else: #if the key or key + hwid isnt in the database at all
    sys("cls") #clear the screen
    print("Password/HWID missmatch") 
    sleep(5)

sys("pause") #wait for user to press key and then exit
