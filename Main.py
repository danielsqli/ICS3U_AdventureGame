import room
import SecretObject
import MagicDoor

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

key1 = SecretObject.SecretObject("Key","Opens a door")

door1 = MagicDoor.MagicDoor(key1)

hallway = room.Room("hallway", "You are in a dimly lit hallway", ["north","west"],["Turn on the lights?","Try to open the door behind you?","Nothing"], ["You can now see better","GHOST ATTACK"],None, None)
closet = room.Room("closet", "You are in a musty closet with 2 jackets in it", ["north", "east"], ["Ruffle through the clothes?","Put on the shoes","Nothing"], ["","GHOST ATTACK","Nothing"], key1, None)
hallway2 = room.Room("hallway","You are in a long hall lit by small lights",["west","north","east","south"], None, None, None, None)
guestRoom = room.Room("guest bedroom", "You are in a small guestroom with 1 bed", ["east"], None, None, None, door1)
washroom = room.Room("washroom", "You are in a bathroom with a sink and a toilet", ["south"], None, None, None, None)
diningRoom = room.Room("dining room","You are in a dining room. The table is set", ["north"], None, None, None, None)
hallway3 = room.Room("hallway", "You are at the end of a hall",["north","east"], None, None, None, None)
kitchen = room.Room("kitchen","You are in a kitchen. There is a whole chicken on the counter",["south","west"],None, None, None, None)
staircase1 = room.Stairs("staircase","You are in a stairwell that leads up",["up"], None, None, None, None, "Stairs")

staircase2 = room.Stairs("staircase","You are in a stairwell that leads up and down",["up", "down"], None, None, None, None,"Stairs")
ladder = room.Stairs("ladder","You found a ladder that leads up",["up"], None, None, None, None, "Stairs")
bathroom = room.Room("bathroom", "You are in a bathroom with a sink, a toilet and a bathtub", ["south"], None, None, None, None)
bedroom = room.Room("master bedroom", "You are in a large bedroom with a bed, a counter, and a fireplace", ["north"], None, None, None, None)
bedroom2 = room.Room("bedroom", "You are in a small bedroom with 1 bed", ["north"], None, None, None, None)
hallway4 = room.Room("hallway", "You are in a thin hallway",["north","west","south"], None, None, None, None)
hallway5 = room.Room("hallway", "You are in a thin hallway",["north","west","south","east"], None, None, None, None)
hallway6 = room.Room("hallway", "You are at the end of a hall",["north","east"], None, None, None, None)
currentRoom = hallway
inventory = []
firstFloor = [[None,washroom,staircase1,None],
              [guestRoom,hallway2,hallway3,kitchen],
              [closet,hallway,None,diningRoom]]

secondFloor = [[ladder, bathroom, staircase2],
               [hallway6,hallway5,hallway4],
               [None,bedroom,bedroom2]]

house = [firstFloor,secondFloor]

currentFloor = firstFloor

while True:


    print(currentRoom.intro())
    if currentRoom.action != None:
        currentRoom.doAction()
    print()
    if currentRoom.type == "Room":
        newRoom = moveRooms(currentRoom,currentFloor)
        while newRoom.magicDoor != None and newRoom.locked(inventory) == True:
            print("The room is locked")
            newRoom = moveRooms(currentRoom, currentFloor)
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
        print(currentRoom.name)

    print("---------------------------------------------------")