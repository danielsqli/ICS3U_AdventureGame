import room
import SecretObject
import MagicDoor
import random
import SecretSwitch

def save(currentRoom, inventory, houseDict, currentFloor, vacuumMastery,checkpointRoom):
    saveFile = open("SaveFile","w")
    saveFile.write("".join(currentRoom.name.split()) + " \n")
    saveFile.write(" ".join(["".join(x.name.split()) for x in inventory if x != None]) + " \n")
    saveFile.write(((list(houseDict.keys())[list(houseDict.values()).index(currentFloor)])) + " \n")
    saveFile.write(str(vacuumMastery) + "\n")
    ghostlessRooms = []
    completedRooms = []
    for i in range(len(currentFloor)):
        for j in range(len(currentFloor[i])):
            if currentFloor[i][j] is not None:
                if currentFloor[i][j].magicDoor is not None:
                    if not currentFloor[i][j].magicDoor.ghost:
                        ghostlessRooms.append("".join(currentFloor[i][j].name.split()))
                if currentFloor[i][j].completed:
                    completedRooms.append("".join(currentFloor[i][j].name.split()))
    saveFile.write(" ".join(ghostlessRooms) + "\n")
    saveFile.write(" ".join(completedRooms) + "\n")
    saveFile.write("".join(currentRoom.name.split()) + " \n")
    saveFile.close()

def loadSave(houseDict,inventoryDict, houseMap):
    saveFile = open("SaveFile","r")
    loadFile = saveFile.readlines()
    currentFloorName = " ".join(loadFile[2].split())
    currentRoomName = " ".join(loadFile[0].split())
    itemNames = loadFile[1].split()
    vacuumMastery = int(loadFile[3])
    currentFloor = houseDict[currentFloorName]
    checkpointRoomName = " ".join(loadFile[6].split())
    inventory = []
    for i in range(len(currentFloor)):
        for j in range(len(currentFloor[i])):
            if currentFloor[i][j] != None:
                if "".join(currentFloor[i][j].name.split()) == currentRoomName:
                    currentRoom = currentFloor[i][j]
                if "".join(currentFloor[i][j].name.split()) == checkpointRoomName:
                    checkpointRoom = currentFloor[i][j]
    completedRooms = "".join(loadFile[5]).split()
    ghostlessRooms = "".join(loadFile[4]).split()
    for i in houseMap:
        for j in range(len(i)):
            for k in range(len(i[j])):
                for l in completedRooms:
                    if i[j][k] is not None and i[j][k].name == l:
                        houseDict[(list(houseDict.keys())[list(houseDict.values()).index(currentFloor)])][j][k].completed = True
                        i[j][k] = houseDict[((list(houseDict.keys())[list(houseDict.values()).index(currentFloor)]))][j][k]
                for p in ghostlessRooms:
                    if i[j][k] is not None and i[j][k].name == p:
                        houseDict[((list(houseDict.keys())[list(houseDict.values()).index(currentFloor)]))][i][k].magicDoor.ghost = False
                        i[j][k] = houseDict[((list(houseDict.keys())[list(houseDict.values()).index(currentFloor)]))][j][k]
    for i in range(len(itemNames)):
        inventory.append(inventoryDict[itemNames[i]])
    saveFile.close()
    return currentFloor,currentRoom,inventory,vacuumMastery,houseMap,checkpointRoom

def moveRooms(currentRoom, floorMap):
    direction = currentRoom.exitWays().lower()[0]
    for i in range(len(floorMap)):
        for j in range(len(floorMap[i])):
            if floorMap[i][j] == currentRoom:
               if direction == "w":
                   return floorMap[i][j-1]
               elif direction == "n":
                   return floorMap[i-1][j]
               elif direction == "e":
                   return floorMap[i][j+1]
               elif direction == "s":
                   return floorMap[i+1][j]

def moveFloors(currentRoom, currentFloor, houseMap):
    direction = currentRoom.exitWays().lower()
    for i in range(len(houseMap)):
        if currentFloor == houseMap[i]:
            if direction == "up":
                return houseMap[i+1]
            if direction == "down":
                return houseMap[i-1]

def ghostAttack(inventory,mastery):
    print("GHOST ATTACK")
    print("WOLOLOLOOOHOHooOHHOH")
    print("The ghost is spooking you")
    print("What to do")
    if vacuum in inventory:
        print("1. Try to attack it \n2. Use the vacuum \n3. Run away \n4. Yell at the ghost")
        while True:
            try:
                choice = int(input("Enter a choice # "))
                break
            except ValueError:
                print("That is not valid")
                continue
        if choice == 1:
            print("You missed")
            return True
        elif choice == 2:
            chance = random.randint(1,100)
            if chance < (mastery//5+1)* 10:
                print("You captured the ghost")
                mastery += 1
                return mastery
        elif choice == 3:
            print("The ghost caught you")
            return True
        elif choice == 4:
            print("It was not very effective")
            return True
    else:
        print("1. Try to attack it \n2. Run away \n3. Yell at the ghost")
        while True:
            try:
                choice = int(input("Enter a choice # "))
                break
            except ValueError:
                print("That is not valid")
                continue
        if choice == 1:
            print("You missed")
        elif choice == 2:
            print("The ghost caught you")
        elif choice == 3:
            print("It was not very effective")
        return True


inventoryDict = {}
guestRoomKey = SecretObject.SecretObject("Guest Room Key","opens a door","was in the jacket pocket")
inventoryDict["GuestRoomKey"] = guestRoomKey
staircaseKey1 = SecretObject.SecretObject("Staircase Key 1", "opens a door","was in the toilet")
inventoryDict['StaircaseKey1'] = staircaseKey1
fork = SecretObject.SecretObject("Fork","looks like it can pick a lock","was on the table")
inventoryDict['Fork'] = fork
bathroomKey1 = SecretObject.SecretObject("Bathroom Key 1","opens a door","was in the chicken")
inventoryDict['BathroomKey1'] = bathroomKey1
ladderKey = SecretObject.SecretObject("Ladder Key","opens a door","fell out of the ceiling")
inventoryDict['LadderKey'] = ladderKey
bedroomKey1 = SecretObject.SecretObject("Bedroom Key 1","opens a door","was in the drawer")
inventoryDict['BedroomKey1'] = bedroomKey1
bedroomKey2 = SecretObject.SecretObject("Bedroom Key 2","opens a door","was on the counter")
inventoryDict['BedroomKey2'] = bedroomKey2
ventilationRoomKey1 = SecretObject.SecretObject('Ventilation Room Key 1','Opens a door','fell out of a box')
inventoryDict['VentilationRoomKey1'] = ventilationRoomKey1
ventilationRoomKey2 = SecretObject.SecretObject('Ventilation Room Key 2','Opens a door','was in the mattress')
inventoryDict['VentilationRoomKey2'] = ventilationRoomKey2
ventilationRoomKey3 = SecretObject.SecretObject('Ventilation Room Key 3','Opens a door','was in the desk')
inventoryDict['VentilationRoomKey3'] = ventilationRoomKey3
bedroomKey3 = SecretObject.SecretObject('Bedroom Key 3','Opens a door','fell out of a box')
inventoryDict['BedroomKey3'] = bedroomKey3
bedroomKey4 = SecretObject.SecretObject('Bedroom Key 4','Opens a door','was on the floor')
inventoryDict['BedroomKey4'] = bedroomKey4
guestRoomKey2 = SecretObject.SecretObject("Guest Room Key 2","opens a door","was in the clothes")
inventoryDict["GuestRoomKey2"] = guestRoomKey2
finalKey1 = SecretObject.SecretObject("Exit Key 1",'Opens a door','bounced onto your face whilst you were jumping on the bed')
inventoryDict['ExitKey1'] = finalKey1
finalKey2 = SecretObject.SecretObject("Exit Key 2",'Opens a door','')
inventoryDict['ExitKey2'] = finalKey2
finalKey3 = SecretObject.SecretObject("Exit Key 3",'Opens a door','')
inventoryDict['ExitKey3'] = finalKey3
finalKey4 = SecretObject.SecretObject("Exit Key 4",'Opens a door','')
inventoryDict['ExitKey4'] = finalKey4

vacuum = SecretObject.SecretObject("Vacuum", "captures ghosts","was behind the bed")

guestRoomDoor = MagicDoor.MagicDoor(guestRoomKey,False)
staircaseDoor1 = MagicDoor.MagicDoor(staircaseKey1, True)
kitchenDoor = MagicDoor.MagicDoor(fork,True)
ladderDoor = MagicDoor.MagicDoor(ladderKey, True)
bathroomDoor1 = MagicDoor.MagicDoor(bathroomKey1, True)
bedroomDoor1 = MagicDoor.MagicDoor([bedroomKey1,bedroomKey2], True)
bedroomDoor2 = MagicDoor.MagicDoor(bedroomKey3,True)
ventilationRoomDoor = MagicDoor.MagicDoor([ventilationRoomKey3,ventilationRoomKey2,ventilationRoomKey1],True)
bedroomDoor3 = MagicDoor.MagicDoor(bedroomKey4,True)
guestRoomDoor2 = MagicDoor.MagicDoor(guestRoomKey2,True)
finalDoor = MagicDoor.MagicDoor([finalKey3,finalKey4,finalKey1,finalKey2],True)

hallway = room.Room("hallway", "You are in a dimly lit hallway", ["north","west"],["Turn on the lights?","Try to open the door behind you?","Nothing"], ["You can now see better","GHOST ATTACK","Nothing"],None, None)
closet = room.Room("closet", "You are in a musty closet with 2 jackets in it", ["north", "east"], ["Ruffle through the clothes?","Put on the shoes","Nothing"], [0,"GHOST ATTACK","Nothing"], guestRoomKey, None)
hallway2 = room.Room("hallway","You are in a long hall lit by small lights",["west","north","east","south"], None, None, None, None)
guestRoom = room.Room("guest bedroom", "You are in a small guestroom with 1 bed", ["east","south"], ["Look behind the bed","Open a drawer","Nothing"], [0,"GHOST ATTACK","Nothing"], vacuum, guestRoomDoor)
washroom = room.Room("washroom", "You are in a bathroom with a sink and a toilet", ["south"], ["Turn on the sink","Stick your hand into the toilet","Use the toilet","Nothing"], ["GHOST ATTACK",0,"GHOST ATTACK","GHOST ATTACK"], staircaseKey1, None)
diningRoom = room.Room("dining room","You are in a dining room. The table is set", ["north"], ["Sit down at the table","Pick up a fork","Break a plate","Nothing"], ["You feel rested",0,"GHOST ATTACK","Nothing"], fork, None)
hallway3 = room.Room("hallway", "You are at the end of a hall",["west","north","east","south"], None, None, None, None)
kitchen = room.Room("kitchen","You are in a kitchen. There is a whole chicken on the counter",["west"],["Eat the chicken","Cut the chicken","Knock the chicken onto the ground","Nothing"], ["GHOST ATTACK",0,"GHOST ATTACK","Nothing"],bathroomKey1, kitchenDoor)
staircase1 = room.Stairs("staircase","You are in a stairwell that leads up",["up"], None, None, None, staircaseDoor1, "Stairs")
newStaircase1 = room.Stairs("staircase","You are in a stairwell that leads up and down",["up","down"], None, None, None, None, "Stairs")
basementSwitch = SecretSwitch.SecretSwitch("Switch",[staircase1,newStaircase1],"You heard a loud shuffling from the first floor")

staircase2 = room.Stairs("staircase","You are in a stairwell that leads down",["down"], None, None, None, None,"Stairs")
ladder = room.Stairs("ladder","You found a ladder that leads up",["up"], None, None, None, ladderDoor, "Stairs")
bathroom = room.Room("bathroom", "You are in a bathroom with a sink, a toilet and a bathtub", ["south"], ["Turn on the shower","Wash your face in the sink","Open the drawer","Nothing"],["GHOST ATTACK","GHOST ATTACK",0,"GHOST ATTACK"], bedroomKey1, bathroomDoor1)
bedroom = room.Room("master bedroom", "You are in a large bedroom with a bed, a counter, and a fireplace", ["north"], ["Turn on the fireplace","Check out the counter","Look under the bed","Nothing"], ["GHOST ATTACK",0,"GHOST ATTACK","Nothing"], bedroomKey2, None)
bedroom2 = room.Room("bedroom", "You are in a small bedroom with 1 bed and a desk", ["north"], ["Jump on the bed","Sit at the desk","Nothing"],[0,"GHOST ATTACK","Nothing"], ladderKey, bedroomDoor1)
hallway4 = room.Room("hallway", "You are in a thin hallway",["north","west","south"], None, None, None, None,"Room",True)
hallway5 = room.Room("hallway", "You are in a thin hallway",["north","west","south","east"], None, None, None, None)
hallway6 = room.Room("hallway", "You are at the end of a hall",["north","east"], None, None, None, None)

ladder2 = room.Stairs("ladder","You found a ladder that leads down",["down"], None, None, None, None, "Stairs")
hallway7 = room.Room("hallway", "You are in a small corridor with a low ceiling",["north","east"], None, None, None, None,'Room',True)
hallway8 = room.Room("hallway",'You are down the hall',['west','east','north'],None, None, None, None)
hallway9 = room.Room("hallway", "You are at a t-junction at the end of a hall",["north","south","west"], None, None, None, None)
hallway10 = room.Room("hallway", "You are at the end of a hall",["south","east"], None, None, None, None)
hallway11 = room.Room("hallway", "You are at the end of a hall",["north","east","west"], None, None, None, None)
storageRoom = room.Room("storage room","You are in a dusty room with a lot of boxes",["south"],["Open one of the boxes",'Kick the boxes over','Turn on the lights','Grab the broom and sweep the floor','Nothing'],['GHOST ATTACK',0,'GHOST ATTACK','The floor has been cleaned','Nothing'],ventilationRoomKey1, None)
bedroom3 = room.Room("bedroom",'You are in an empty bedroom with an empty bed frame',['west'],['Look into the bed frame','Place one of the conveniently placed mattresses into the bedframe','Take one of the pillow covers','Nothing'],['GHOST ATTACK',0,1,'Nothing'],[ventilationRoomKey2,bedroomKey3],None)
bedroom4 = room.Room("bedroom",'You are in a small bedroom with only a chair and desk',['west'],['Sit on the chair','Split the desk in half with your hands','Stab the wall with your fork in anger','Nothing'],['GHOST ATTACK',0,'GHOST ATTACK','Nothing'],ventilationRoomKey3,None)
ventilationRoom = room.Room("ventilation room","You are in a long room with fans that lead to outside the house",['east'],['Check behind a fan','Stick your hand in a fan','Hit one of the fans','Nothing'],['GHOST ATTACK',0,'GHOST ATTACK','Nothing'],basementSwitch,ventilationRoomDoor)

staircase3 = room.Stairs("staircase","You found a staircase that leads up",["up"], None, None, None, None, "Stairs")
hallway12 = room.Room("hallway",'You are in a hallway with wooden walls',['north','south','west'],None, None, None, None,"Room",True)
hallway13 = room.Room("hallway",'You are in a hallway with wooden walls',['north','west','east','south'],None, None, None, None)
laundryRoom = room.Room("laundry room",'You are in a laundry room with a washer and a dryer',['north'],['Open the washer','Open the dryer','Kick the basket over','Nothing'],['GHOST ATTACK','GHOST ATTACK',"GHOST ATTACK",0],bedroomKey4,None)
bedroom5 = room.Room("bedroom",'You are in a bedroom with a clothes rack and a bed',['south'],['Take down a shirt','Jump on the bed','Kick the clothes rack over','Nothing'],['GHOST ATTACK',0,1,'Nothing'],[finalKey1,guestRoomKey2],bedroomDoor3)
guestRoom2 = room.Room("guest room",'You are in a guest room with a pile of clothes on the ground',['north'],['Jump into the pile','Scratch your head in confusion','Vacuum up the clothes','Nothing'],['GHOST ATTACK','GHOST ATTACK',0,'Nothing'],finalKey2,guestRoomDoor2)
hallway14 = room.Room("hallway",'You are in a short hallway with doors on all sides',['north','east','south','west'],None, None, None, None)
washroom2 = room.Room('washroom','You are in a dusty washroom with a broken sink and toilet',['south'],['Try to turn on the sink','Sit on the toilet','Flush the toilet','Nothing'],['GHOST ATTACK',0,'GHOST ATTACK','Nothing'],finalKey3,None)
closet2 = room.Room('closet','You are in an empty closet',['north'],['Do chin ups on the bars','Yell at the top of your lungs','Admire your keychain','Nothing'],[0,'GHOST ATTACK','GHOST ATTACK','Nothing'],finalKey4,None)
finalExit = room.Room('exit','You are finally outside',None,None,None,None,finalDoor)


currentRoom = hallway
checkPointRoom = hallway

firstFloor = [[None,washroom,staircase1,None],
              [guestRoom,hallway2,hallway3,kitchen],
              [closet,hallway,diningRoom,None]]

secondFloor = [[ladder, bathroom, staircase2],
               [hallway6,hallway5,hallway4],
               [None,bedroom,bedroom2]]

attic = [[ladder2, storageRoom, hallway10, bedroom3],
         [hallway7, hallway8, hallway9, None],
         [None, ventilationRoom, hallway11, bedroom4]]

basement = [[None, washroom2, bedroom5,staircase3],
            [finalExit,hallway14,hallway13,hallway12],
            [None,closet2,guestRoom2,laundryRoom]]

houseDict = {"First Floor":firstFloor,"Second Floor":secondFloor,"Attic":attic,"Basement":basement}
house = [basement, firstFloor,secondFloor,attic]
currentFloor = firstFloor
checkPointRoom = hallway
inventory = []
vacuumMastery = 0
death = False
victory = False

print("Do you want to load the save? (y/n)")
choice = input()
while choice.lower() not in ['y', 'n', 'yes', 'no']:
    choice = input("That is not valid. Re-enter: ")
if choice.lower() in ['y','yes']:
    values = loadSave(houseDict,inventoryDict,house)
    currentFloor,currentRoom,inventory,vacuumMastery,house,checkPointRoom = values



while True:
    print("---------------------------------------------------")
    print(currentRoom.intro())
    if currentRoom.checkPoint == True:
        print("You have reached a checkpoint")
        checkPointRoom == currentRoom
        currentRoom.checkPoint = False
    if currentRoom.action != None:
        result = currentRoom.doAction(inventory)
        if result == "win":
            victory = True
            break
        if result == "Save":
            print("Do you want to save the game? (y/n)")
            choice = input()
            while choice.lower() not in ['y','n','yes','no']:
                choice = input("That is not valid. Re-enter: ")
            if choice.lower() in ['y','yes']:
                save(currentRoom,inventory,houseDict,currentFloor,vacuumMastery,checkPointRoom)
                saved = True
                break
        elif result == "switch":
            currentRoom.secretItem.discovery()
            house = currentRoom.secretItem.action(house)
        elif type(result) == int:
            if type(currentRoom.secretItem) == list:
                print(currentRoom.secretItem[result])
                inventory.append(currentRoom.secretItem[result])
            else:
                print(currentRoom.secretItem)
                inventory.append(currentRoom.secretItem)
        elif result:
            if ghostAttack(inventory,vacuumMastery):
                currentRoom = checkPointRoom
                print("You were defeated...")
                input("*press enter to continue*")
                continue
            else:
                vacuumMastery += 1
                print("The ghost was sucked into the vacuum")



    print()
    if currentRoom.type == "Room":
        newRoom = moveRooms(currentRoom,currentFloor)
        while newRoom.magicDoor != None and newRoom.locked(inventory) == True:
            print("The room is locked")
            if newRoom.magicDoor.ghost != None:
                result = ghostAttack(inventory,vacuumMastery)
                if type(result) == int:
                    vacuumMastery = result
                    newRoom.magicDoor.ghost = False
                    print("The door unlocked itself")
                    break
                else:
                    currentRoom = checkPointRoom
                    print("You were defeated")
                    print("press enter to continue")
                    death = True
                    break
            newRoom = moveRooms(currentRoom, currentFloor)
        if death == True:
            death = False
            continue
        currentRoom = newRoom
    elif currentRoom.type == "Stairs":
        for row in range(len(currentFloor)):
            try:
                column = currentFloor[row].index(currentRoom)
                break
            except ValueError:
                continue
        currentFloor = moveFloors(currentRoom, currentFloor,house)
        currentRoom = currentFloor[row+1][column]

if victory == True:
    from colorama import init
    from termcolor import cprint
    from pyfiglet import figlet_format

    cprint(figlet_format("VICTORY", font='starwars'),
           'red', 'on_white', attrs=['bold'])

