#ServerCheck.py © 2022 by UsLpH is licensed under CC BY-NC-SA 4.0
#https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1


from asyncio.windows_events import NULL
import os
import ctypes
os.system("title UsLpH's server checker       UsLpH#0001")
from xmlrpc.client import Server
import requests
import time
import re
import math
from colorama import Fore, Back, Style
Fine = True
os.system("cls")




SteamID = []
def Search(naame):
    s = requests.Session()
    s.get("https://steamcommunity.com")
    payload = {
        'text': naame,
        'filter': 'users'
    }
    res = s.post("https://steamcommunity.com/search/SearchCommunityAjax?text=" + naame + "&filter=users&sessionid=" + s.cookies['sessionid']  + "&steamid_user=false", json=payload)
    return res


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

while True:
    while True:
        avrg = 0
        os.system("cls")
        print("Enter Server ID :", end="")
        Sin = input()
        w = requests.get("https://www.battlemetrics.com/servers/rust/" + Sin)
        os.system("cls")

        s = 0
        total = 0
        PlayerIDs = re.findall(r'(?<=","player_id":").+?(?=","server_id":"' + Sin + r'")', w.text)
        IdsLength = len(PlayerIDs)
        h = 0
        while (h < IdsLength):
            Boobs = ""
            IdsLength = len(PlayerIDs)
            spoofed = False
            asdsad = "profiles"
            w = requests.get("https://www.battlemetrics.com/players/" + PlayerIDs[h])
            if ("This player has been seen on over 250 servers. Due to the number of servers this player has been on we are only displaying the most recent 250 servers." in w.text):
                Boobs = " Innacurate Hour Data"
            total = 0
            res = re.findall(r'(?<=\"timePlayed\":).+?(?=})', w.text)
            reb = re.findall(r'(?<={\"serverId\":\").+?(?=\",\")', w.text)
        
            re.findall(r'(?<={"id":"' + PlayerIDs[h] + r'","name":").+?(?=","createdAt":)', w.text)
            i = 0
            while (i <= len(res)-1):
                if ("\"id\":\"" + reb[i] +"\",\"game_id\":\"rust\"" in w.text):
                    total = total + int(res[i])
                i += 1
            Hours = str((total/60)/60).split(".")[0]
            avrg += int(Hours)
            BMname = re.findall(r'(?<={"id":"'+ PlayerIDs[h] +'","name":").+?(?=","createdAt")', w.text)
            
            FirstSeen = re.findall(r'(?<=AM">).+?(?=</time></dd><dt>Last Seen</dt><dd>)', w.text)
            if (FirstSeen == []):
                FirstSeen = re.findall(r'(?<=PM">).+?(?=</time></dd><dt>Last Seen</dt><dd>)', w.text)
                if (FirstSeen == []):
                    print("ERROR")
                else:
                    FirstSeen = FirstSeen[0]
            else:
                FirstSeen = FirstSeen[0]
            

            session = Search(BMname[0])
            SteamID = re.findall(r'(?<=href=\\"https:\\\/\\\/steamcommunity.com\\\/profiles\\\/).+?(?=\\\">)', session.text)
            yo = False
            if (SteamID == []):
                SteamID = re.findall(r'(?<=href=\\"https:\\\/\\\/steamcommunity.com\\\/id\\\/).+?(?=\\\">)', session.text)
                asdsad = "id"
                if (SteamID != NULL):
                    yo = True
            if (SteamID):
                if (yo):
                    FirstSeen = re.findall(r'(?<=<span id="membersince">).+?(?=</span>)',requests.get("http://steamrep.com/search?q=https%3A%2F%2Fsteamcommunity.com%2Fid%2F" + SteamID[0]).text)[0]
                else:
                    FirstSeen = re.findall(r'(?<=<span id="membersince">).+?(?=</span>)',requests.get("http://steamrep.com/search?q=" + SteamID[0]).text)[0]

                if (int(Hours) < 500):
                    print(Fore.YELLOW, end="")
                    if (int(Hours) < 100):
                        print(Fore.RED, end="")

                if (len(SteamID) < 5):
                    if (len(SteamID) == 2):
                        print(FirstSeen + " " + BMname[0] + " has " + Hours + " hours. " + Boobs + Fore.GREEN + "https://steamcommunity.com/" + asdsad + "/" + SteamID[0])
                    else:
                        print(FirstSeen + " " +BMname[0] + " has " + Hours + " hours. "+ Boobs + Style.RESET_ALL + " https://steamcommunity.com/" + asdsad + "/" + SteamID[0])
                else:
                    print(BMname[0] + " has " + Hours + " hours." + Boobs)
            else:
                print(BMname[0] + " has " + Hours + " hours." + Boobs)
            print(Style.RESET_ALL, end="")
            if (h == IdsLength - 1):
                avrg = avrg/len(PlayerIDs)
                avrg = str(avrg).split(".")[0]
                print("\n\nAverage Hours : " + avrg)
                print("Player Count : " + str(len(PlayerIDs)) + "\n\n")
            h+=1
        os.system("pause")
