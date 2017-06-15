import room
import SecretObject
import MagicDoor
import random

def save(currentRoom, inventory, houseDict, currentFloor, vacuumMastery):
    saveFile = open("SaveFile","w")
    saveFile.write(currentRoom.name + " \n")
    saveFile.write(" ".join([x.name for x in inventory if x != None]) + " \n")
    saveFile.write(((list(houseDict.keys())[list(houseDict.values()).index(currentFloor)])) + " \n")
    saveFile.write(str(vacuumMastery) + "\n")
    ghostlessRooms = []
    completedRooms = []
    for i in range(len(currentFloor)):
        for j in range(len(currentFloor[i])):
            if currentFloor[i][j] is not None:
                if currentFloor[i][j].magicDoor is not None:
                    if not currentFloor[i][j].magicDoor.ghost:
                        ghostlessRooms.append(currentFloor[i][j].name)
                if currentFloor[i][j].completed:
                    completedRooms.append(currentFloor[i][j].name)
    saveFile.write(" ".join(ghostlessRooms) + "\n")
    saveFile.write(" ".join(completedRooms) + "\n")
    saveFile.close()

def loadSave(houseDict,inventoryDict, houseMap):
    saveFile = open("SaveFile","r")
    loadFile = saveFile.readlines()
    currentFloorName = " ".join(loadFile[2].split())
    currentRoomName = " ".join(loadFile[0].split())
    itemNames = loadFile[1].split()
    vacuumMastery = int(loadFile[3])
    currentFloor = houseDict[currentFloorName]
    inventory = []
    for i in range(len(currentFloor)):
        for j in range(len(currentFloor[i])):
            if currentFloor[i][j] != None:
                if currentFloor[i][j].name == currentRoomName:
                    currentRoom = currentFloor[i][j]
    completedRooms = loadFile[5]
    ghostlessRooms = loadFile[4]
    for i in houseMap:
        for j in range(len(i)):
            for k in range(len(i[j])):
                for l in completedRooms:
                    if i[j][k] is not None and i[j][k].name == l:
                        houseDict[l].completed = True
                        i[j][k] = houseDict[l]
                for p in ghostlessRooms:
                    if i[j][k] is not None and i[j][k].name == p:
                        houseDict[p].magicDoor.ghost = False
                        i[j][k] = houseDict[l]
    for i in range(len(itemNames)):
        inventory.append(inventoryDict[itemNames[i]])
    saveFile.close()
    return currentFloor,currentRoom,inventory,vacuumMastery

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
        choice = int(input("Enter a choice # "))
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
        choice = int(input("Enter a choice # "))
        if choice == 1:
            print("You missed")
        elif choice == 2:
            print("The ghost caught you")
        elif choice == 3:
            print("It was not very effective")
        return True

inventoryDict = {}
guestRoomKey = SecretObject.SecretObject("Guest Room Key","opens a door","was in the jacket pocket")
inventoryDict["Guest Room Key"] = guestRoomKey
staircaseKey1 = SecretObject.SecretObject("Staircase Key 1", "opens a door","was in the toilet")
inventoryDict['Staircase Key 1'] = staircaseKey1
fork = SecretObject.SecretObject("Fork","looks like it can pick a lock","was on the table")
inventoryDict['Fork'] = fork
bathroomKey1 = SecretObject.SecretObject("Bathroom Key 1","opens a door","was in the chicken")
inventoryDict['Bathroom Key 1'] = bathroomKey1
ladderKey = SecretObject.SecretObject("Ladder Key","opens a door","was")
inventoryDict['Ladder Key'] = ladderKey
bedroomKey1 = SecretObject.SecretObject("Bedroom Key 1","opens a door","was in the drawer")
inventoryDict['Bedroom Key 1'] = bedroomKey1
bedroomKey2 = SecretObject.SecretObject("Bedroom Key 2","opens a door","was ")
inventoryDict['Bedroom Key 2'] = bedroomKey2


vacuum = SecretObject.SecretObject("Vacuum", "captures ghosts","was behind the bed")

guestRoomDoor = MagicDoor.MagicDoor(guestRoomKey,None)
staircaseDoor1 = MagicDoor.MagicDoor(staircaseKey1, True)
kitchenDoor = MagicDoor.MagicDoor(fork,True)
ladderDoor = MagicDoor.MagicDoor(ladderKey, True)
bathroomDoor1 = MagicDoor.MagicDoor(bathroomKey1, True)
bedroomDoor1 = MagicDoor.MagicDoor([bedroomKey1,bedroomKey2], True)


hallway = room.Room("hallway", "You are in a dimly lit hallway", ["north","west"],["Turn on the lights?","Try to open the door behind you?","Nothing"], ["You can now see better","GHOST ATTACK","Nothing"],None, None)
closet = room.Room("closet", "You are in a musty closet with 2 jackets in it", ["north", "east"], ["Ruffle through the clothes?","Put on the shoes","Nothing"], ["","GHOST ATTACK","Nothing"], guestRoomKey, None)
hallway2 = room.Room("hallway","You are in a long hall lit by small lights",["west","north","east","south"], None, None, None, None)
guestRoom = room.Room("guest_bedroom", "You are in a small guestroom with 1 bed", ["east","south"], ["Look behind the bed","Open a drawer","Nothing"], ["","GHOST ATTACK","Nothing"], vacuum, guestRoomDoor)
washroom = room.Room("washroom", "You are in a bathroom with a sink and a toilet", ["south"], ["Turn on the sink","Stick your hand into the toilet","Use the toilet","Nothing"], ["GHOST ATTACK","","GHOST ATTACK","GHOST ATTACK"], staircaseKey1, None)
diningRoom = room.Room("dining_room","You are in a dining room. The table is set", ["north"], ["Sit down at the table","Pick up a fork","Break a plate","Nothing"], ["You feel rested","","GHOST ATTACK","Nothing"], fork, None)
hallway3 = room.Room("hallway", "You are at the end of a hall",["north","east","south"], None, None, None, None)
kitchen = room.Room("kitchen","You are in a kitchen. There is a whole chicken on the counter",["west"],["Eat the chicken","Cut the chicken","Knock the chicken onto the ground","Nothing"], ["GHOST ATTACK","","GHOST ATTACK","Nothing"],bathroomKey1, kitchenDoor)
staircase1 = room.Stairs("staircase","You are in a stairwell that leads up",["up"], None, None, None, staircaseDoor1, "Stairs", True)

staircase2 = room.Stairs("staircase","You are in a stairwell that leads up and down",["up", "down"], None, None, None, None,"Stairs")
ladder = room.Stairs("ladder","You found a ladder that leads up",["up"], None, None, None, ladderDoor, "Stairs")
bathroom = room.Room("bathroom", "You are in a bathroom with a sink, a toilet and a bathtub", ["south"], ["Turn on the shower","Wash your face in the sink","Open the drawer","Nothing"],["GHOST ATTACK","GHOST ATTACK","","GHOST ATTACK"], bedroomKey1, bathroomDoor1)
bedroom = room.Room("master_bedroom", "You are in a large bedroom with a bed, a counter, and a fireplace", ["north"], ["Turn on the fireplace","Check out the counter","Look under the bed","Nothing"], ["GHOST ATTACK","","GHOST ATTACK","Nothing"], bedroomKey2, None)
bedroom2 = room.Room("bedroom", "You are in a small bedroom with 1 bed", ["north"], None, None, None, bedroomDoor1)
hallway4 = room.Room("hallway", "You are in a thin hallway",["north","west","south"], None, None, None, None)
hallway5 = room.Room("hallway", "You are in a thin hallway",["north","west","south","east"], None, None, None, None)
hallway6 = room.Room("hallway", "You are at the end of a hall",["north","east"], None, None, None, None)
currentRoom = hallway
checkPointRoom = hallway

firstFloor = [[None,washroom,staircase1,None],
              [guestRoom,hallway2,hallway3,kitchen],
              [closet,hallway,diningRoom,None]]

secondFloor = [[ladder, bathroom, staircase2],
               [hallway6,hallway5,hallway4],
               [None,bedroom,bedroom2]]

houseDict = {"First Floor":firstFloor,"Second Floor":secondFloor}
house = [firstFloor,secondFloor]

currentFloor = firstFloor

inventory = []
vacuumMastery = 0
death = False
print("Do you want to load the save? (y/n)")
choice = input()
while choice.lower() not in ['y', 'n', 'yes', 'no']:
    choice = input("That is not valid. Re-enter: ")
if choice.lower() in ['y','yes']:
    values = loadSave(houseDict,inventoryDict,house)
    currentFloor,currentRoom,inventory,vacuumMastery = values
while True:

    print("---------------------------------------------------")
    print(currentRoom.intro())
    if currentRoom.checkPoint == True:
        print("You have reached a checkpoint")
        checkPointRoom == currentRoom
        currentRoom.checkPoint = False
    if currentRoom.action != None:
        result = currentRoom.doAction()
        if result == "Save":
            print("Do you want to save the game? (y/n)")
            choice = input()
            while choice.lower() not in ['y','n','yes','no']:
                choice = input("That is not valid. Re-enter: ")
            if choice.lower() in ['y','yes']:
                save(currentRoom,inventory,houseDict,currentFloor,vacuumMastery)
                saved = True
                break
        elif not result:
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

