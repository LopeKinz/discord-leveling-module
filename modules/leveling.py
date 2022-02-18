import json
import discord


    
    
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