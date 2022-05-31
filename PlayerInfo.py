#PlayerInfo.py © 2022 by UsLpH is licensed under CC BY-NC-SA 4.0
#https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1
import os
os.system("title UsLpH's player info       UsLpH#0001")
from xmlrpc.client import Server
import requests
import re
import math
Fine = True

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


private = False

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
id = False

SteamIDFound = False

while True:
    while True:
        Boobs = ""
        os.system("cls")
        print("Is player online? (y/n) :", end="")
        Online = input()
        if (Online == "y"):
            print("Enter Username : ", end="")
            Sin = input()
            w = requests.get("https://www.battlemetrics.com/players?filter%5Bsearch%5D=\"" + Sin + "\"&filter%5Bonline%5D=true&filter%5BplayerFlags%5D=&filter%5Bserver%5D%5Bgame%5D=rust&sort=-lastSeen")
        elif (Online == "n"):
            print("Enter Username : ", end="")
            Sin = input()
            w = requests.get("https://www.battlemetrics.com/players?filter%5Bsearch%5D=\"" + Sin + "\"&filter%5Bonline%5D=false&filter%5BplayerFlags%5D=&sort=-lastSeen")
        else:
            os.system("cls")
            print("Please Enter y or n.\n")
            os.system("pause")
            break
        Split1 = w.text.split("\"},\"itemIds\":[\"")
        try:
            Split2 = Split1[1].split("\"")
        except IndexError:
            os.system("cls")
            print("Player Not Found.\n")
            
            os.system("pause")
            break
        r = requests.get('https://www.battlemetrics.com/players/'+ Split2[0] + "/")
        if ("This player has been seen on over 250 servers. Due to the number of servers this player has been on we are only displaying the most recent 250 servers." in r.text):
            Boobs = " Innacurate Hour Data"

        os.system("cls")
        s = 0
        total = 0
        ServerName = re.findall(r'(?<=><a href="/servers/rust/).+?(?=<\/a>)', r.text)
        try:
            ServerRust = ServerName[0].split("\">")[1]
        except IndexError:
            ServerRust = "Not Connected To Server"
        res = re.findall(r'(?<=\"timePlayed\":).+?(?=})', r.text)
        reb = re.findall(r'(?<={\"serverId\":\").+?(?=\",\")', r.text)
        
        FirstSeen = re.findall(r'(?<=AM">).+?(?=</time></dd><dt>Last Seen</dt><dd>)', r.text)
        if (FirstSeen == []):
            FirstSeen = re.findall(r'(?<=PM">).+?(?=</time></dd><dt>Last Seen</dt><dd>)', r.text)
            if (FirstSeen == []):
                print("ERROR")
        FirstSeen = FirstSeen[0]
        i = 0
        while (i <= len(res)-1):
            if ("\"id\":\"" + reb[i] +"\",\"game_id\":\"rust\"" in r.text):
                total = total + int(res[i])
                s += 1
            i += 1
        Hours = str((total/60)/60).split(".")[0]
        BMname = re.findall(r'(?<={"id":"'+ Split2[0] +'","name":").+?(?=","createdAt")', w.text)
       
        session = Search(BMname[0])
        if ("This profile is private." in session.text):
            private = True
        SteamID = re.findall(r'(?<=href=\\"https:\\\/\\\/steamcommunity.com\\\/profiles\\\/).+?(?=\\\">)', session.text)
        yo = False
        if (SteamID == []):
            SteamID = re.findall(r'(?<=href=\\"https:\\\/\\\/steamcommunity.com\\\/id\\\/).+?(?=\\\">)', session.text)
            yo = True
        if (SteamID):
            if (len(SteamID) > 3):
                SteamID[0] = ""
                SteamIDFound = False
            else:
                SteamIDFound = True
                if (yo):
                    FirstSeen = re.findall(r'(?<=<span id="membersince">).+?(?=</span>)',requests.get("http://steamrep.com/search?q=https%3A%2F%2Fsteamcommunity.com%2Fid%2F" + SteamID[0]).text)[0]
                else:
                    FirstSeen = re.findall(r'(?<=<span id="membersince">).+?(?=</span>)',requests.get("http://steamrep.com/search?q=" + SteamID[0]).text)[0]
                    
        yes = requests.get('https://steamcommunity.com/profiles/' + SteamID[0]) 
        if ("Sorry!" in yes.text):
            id = True
        else:
            yeSs = requests.get('https://steamcommunity.com/id/' + SteamID[0]) 
            if ("Sorry!" in yeSs.text):
                id = False

        if (SteamIDFound): 
            if (id):
                print("https://steamcommunity.com/id/" + SteamID[0])
                if (private):
                    print("Private")
                else:
                    print("Steam Level " + re.findall(r'(?<=<span class="friendPlayerLevelNum">).+?(?=</span></div></div>)', requests.get("https://steamcommunity.com/id/" + SteamID[0]).text)[0])      
            else:
                print("https://steamcommunity.com/profile/" + SteamID[0])
                if (private):
                    print("Private")
                else:
                    print( "Steam Level " + re.findall(r'(?<=<span class="friendPlayerLevelNum">).+?(?=</span></div></div>)', requests.get("https://steamcommunity.com/profiles/" + SteamID[0]).text)[0])      
        print ("Started " + FirstSeen)
        print ("Battle Metrics Name : " + BMname[0] + "\n\n")
        print ("Player has played on " + str(s) + " different servers.\n" + "Player has " + Hours + " hours. " + Boobs + "\n")
        print ("BattleMetrics Profile : https://www.battlemetrics.com/players/" + Split2[0])
 
        print ("Current server : " + ServerRust)
        print("\n")
        os.system("pause")

