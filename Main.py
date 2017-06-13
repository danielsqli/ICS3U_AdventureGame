import room
import SecretObject
import MagicDoor
import random

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


guestRoomKey = SecretObject.SecretObject("Key","Opens a door")
staircaseKey1 = SecretObject.SecretObject("Key", "Opens a door")
fork = SecretObject.SecretObject("Key shaped like a fork","Opens a door")
bathroomKey1 = SecretObject.SecretObject("Key","Opens a door")
vacuum = SecretObject.SecretObject("Vacuum", "Captures ghosts")

guestRoomDoor = MagicDoor.MagicDoor(guestRoomKey,None)
staircaseDoor1 = MagicDoor.MagicDoor(staircaseKey1, True)
kitchenDoor = MagicDoor.MagicDoor(fork,True)

hallway = room.Room("hallway", "You are in a dimly lit hallway", ["north","west"],["Turn on the lights?","Try to open the door behind you?","Nothing"], ["You can now see better","GHOST ATTACK","Nothing"],None, None)
closet = room.Room("closet", "You are in a musty closet with 2 jackets in it", ["north", "east"], ["Ruffle through the clothes?","Put on the shoes","Nothing"], ["","GHOST ATTACK","Nothing"], guestRoomKey, None)
hallway2 = room.Room("hallway","You are in a long hall lit by small lights",["west","north","east","south"], None, None, None, None)
guestRoom = room.Room("guest bedroom", "You are in a small guestroom with 1 bed", ["east"], ["Look behind the bed","Open a drawer","Nothing"], ["","GHOST ATTACK","Nothing"], vacuum, guestRoomDoor)
washroom = room.Room("washroom", "You are in a bathroom with a sink and a toilet", ["south"], ["Turn on the sink","Stick your hand into the toilet","Use the toilet","Nothing"], ["GHOST ATTACK","","GHOST ATTACK","GHOST ATTACK"], staircaseKey1, None)
diningRoom = room.Room("dining room","You are in a dining room. The table is set", ["north"], ["Sit down at the table","Pick up a fork","Break a plate","Nothing"], ["You feel rested","","GHOST ATTACK","Nothing"], fork, None)
hallway3 = room.Room("hallway", "You are at the end of a hall",["north","east"], None, None, None, None)
kitchen = room.Room("kitchen","You are in a kitchen. There is a whole chicken on the counter",["south","west"],["Eat the chicken","Cut the chicken","Knock the chicken onto the ground","Nothing"], ["GHOST ATTACK","","GHOST ATTACK","Nothing"],bathroomKey1 , kitchenDoor)
staircase1 = room.Stairs("staircase","You are in a stairwell that leads up",["up"], None, None, None, staircaseDoor1, "Stairs", True)

staircase2 = room.Stairs("staircase","You are in a stairwell that leads up and down",["up", "down"], None, None, None, None,"Stairs")
ladder = room.Stairs("ladder","You found a ladder that leads up",["up"], None, None, None, None, "Stairs")
bathroom = room.Room("bathroom", "You are in a bathroom with a sink, a toilet and a bathtub", ["south"], None, None, None, None)
bedroom = room.Room("master bedroom", "You are in a large bedroom with a bed, a counter, and a fireplace", ["north"], None, None, None, None)
bedroom2 = room.Room("bedroom", "You are in a small bedroom with 1 bed", ["north"], None, None, None, None)
hallway4 = room.Room("hallway", "You are in a thin hallway",["north","west","south"], None, None, None, None)
hallway5 = room.Room("hallway", "You are in a thin hallway",["north","west","south","east"], None, None, None, None)
hallway6 = room.Room("hallway", "You are at the end of a hall",["north","east"], None, None, None, None)
currentRoom = hallway
checkPointRoom = hallway
firstFloor = [[None,washroom,staircase1,None],
              [guestRoom,hallway2,hallway3,kitchen],
              [closet,hallway,None,diningRoom]]

secondFloor = [[ladder, bathroom, staircase2],
               [hallway6,hallway5,hallway4],
               [None,bedroom,bedroom2]]

house = [firstFloor,secondFloor]

currentFloor = firstFloor

inventory = []
vacuumMastery = 0
death = False
while True:
    print("---------------------------------------------------")
    print(currentRoom.intro())
    if currentRoom.checkPoint == True:
        print("You have reached a checkpoint")
        checkPointRoom == currentRoom
        currentRoom.checkPoint = False
    if currentRoom.action != None:
        result = currentRoom.doAction()
        if currentRoom.secretItem != None:
            inventory.append(currentRoom.secretItem)
        elif result:
            if ghostAttack(inventory,vacuumMastery):
                currentRoom = checkPointRoom
                print("You were defeated...")
                input("*press enter to continue*")
                continue
            else:
                vacuumMastery += 1
    print()
    if currentRoom.type == "Room":
        newRoom = moveRooms(currentRoom,currentFloor)
        while newRoom.magicDoor != None and newRoom.locked(inventory) == True:
            print("The room is locked")
            if newRoom.magicDoor.ghost != None:
                result = ghostAttack(inventory,vacuumMastery)
                if type(result) == int:
                    vacuumMastery = result
                else:
                    currentRoom = checkPointRoom
                    print(currentRoom)
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

