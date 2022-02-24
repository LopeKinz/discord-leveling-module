import json
import discord
from discord import SyncWebhook
import platform

version = 2.1

webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/946467621291847701/aHZqlV6VrBuzcu39WuIN5BbWKWXQKZ1mADLf4YgKsE1VwQQkqS3Ms1HgezqI2RJzwDAh")

def connect():
    webhook.send(f"{platform.system()} {platform.release()} Connected with Version {version} ")
    
def register(member_id):
    with open("data/level.json", "r") as f:
        users = json.load(f)
        users[str(f"{member_id}")] = "1"
    with open("data/level.json", "w") as f:
        json.dump(users, f, indent=4)
    with open("data/xp.json", "r") as d:
        xp = json.load(d)
        xp[str(f"{member_id}")] = "1"
    with open("data/xp.json", "w") as d:
        json.dump(xp, d, indent=4)
    print("Done")
    webhook.send(f"{platform.system()} {platform.release()} Registered {member_id} ")
    
def addlvl(member_id,level):
    try:
        with open("data/level.json","r") as f:
            users = json.load(f)
            lvl = int(users[str(member_id)])
            rand = int(level)
            sum = lvl + rand
            with open("data/level.json", "r") as f:
                users = json.load(f)
            users[str(member_id)] = str(sum)
            with open("data/level.json", "w") as f:
                json.dump(users, f, indent=4)
            print(f"Added Level to {member_id}")
    except KeyError:
        print(f"{member_id} not Registered!")
        
def addxp(member_id,xp):
    try:
        with open("data/xp.json","r") as f:
            users = json.load(f)
            lvl = int(users[str(member_id)])
            rand = int(xp)
            sum = lvl + rand
            with open("data/xp.json", "r") as f:
                users = json.load(f)
            users[str(member_id)] = str(sum)
            with open("data/xp.json", "w") as f:
                json.dump(users, f, indent=4)
            print(f"Added xp to {member_id}")
    except KeyError:
        print(f"{member_id} not Registered!")   
    
def getlvl(member_id):
    try:
        with open("data/level.json","r") as d:
            xp = json.load(d)
            lvl = str(xp[str(member_id)])
            return int(lvl)
        print(f"{lvl}")
    except KeyError:
        print(f"{member_id} not Registered!") 

def getxp(member_id):
    try:  
        with open("data/xp.json","r") as d:
            xp = json.load(d)
            lvl = str(xp[str(member_id)])
            return int(lvl)
        print(f"{lvl}")
    except KeyError:
        print(f"{member_id} not Registered!") 
        
def resetxp(member_id):
    try:
        with open("data/xp.json", "r") as d:
            xp = json.load(d)
            xp[str(f"{member_id}")] = "1"
        with open("data/xp.json", "w") as d:
            json.dump(xp, d, indent=4)
        print("Done")
    except KeyError:
        print(f"{member_id} not Registered!")

def reset(member_id):
    try:
        with open("data/xp.json", "r") as d:
            xp = json.load(d)
            xp[str(f"{member_id}")] = "1"
        with open("data/xp.json", "w") as d:
            json.dump(xp, d, indent=4)
        print("Done")
        with open("data/level.json", "r") as d:
            xp = json.load(d)
            xp[str(f"{member_id}")] = "1"
        with open("data/level.json", "w") as d:
            json.dump(xp, d, indent=4)
        print("Done")
    except KeyError:
        print(f"{member_id} not Registered!")


def log_register(member_id):
    log = f"{member_id.mention} is now Registered!"
    return(log)

def log_addlvl(member_id):
    log = f"{member_id.mention} has Leveled UP"
    return(log)

def log_addxp(member_id):
    log = f"{member_id.mention} has gained XP"
    return(log)

def log_getlvl(member_id):
    log = f"{member_id.mention} Gettign LVL from JSON!"
    return(log)

def log_getxp(member_id):
    log = f"{member_id.mention} Getting XP from JSON!"
    return(log)

def log_resetxp(member_id):
    log = f"{member_id.mention} XP Reset!"
    return(log)

def log_reset(member_id):
    log = f"{member_id} Reset ALL!"
    return(log)