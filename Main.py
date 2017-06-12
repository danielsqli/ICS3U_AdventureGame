import room
import SecretObject
import MagicDoor
def moveRooms(currentRoom, floorMap):
    direction = currentRoom.exitWays()
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




key1 = SecretObject.SecretObject("Key","door")
door1 = MagicDoor.MagicDoor(key1)
hallway = room.Room("hallway", "You are in a dimly lit hallway", ["north","west","n","w"], "There is a light switch. Turn on the lights?", "You can now see better",None,None)
closet = room.Room("closet", "You are in a musty closet with 2 jackets in it", ["north", "east","e", "n"], "Ruffle through the clothes?", "Already found key", key1,None)
hallway2 = room.Room("hallway","You are in a long hall lit by small lights",["west","north","east","south","w","n","e","s"], None, None, None,None)
guestRoom = room.Room("guest bedroom", "You are in a small guestroom with 1 bed", ["east","e"], None, None, None,None)
bathroom1 = room.Room("bathroom", "You are in a a bathroom with a sink and a toilet", ["south","s"], None, None, None,None)
diningRoom = room.Room("dining room", "You are in a dining room with a table that has plates at every seat", ["east","north","e","n"], None, None, None,None)
kitchen = room.Room("kitchen", "You are in a kitchen with a whole chicken on a cutting board",["north","west","n","w"],None,None,None,door1)
currentRoom = hallway
inventory = []
firstFloor = [[None,bathroom1,2,None],[guestRoom,hallway2,5,6],[closet,hallway,diningRoom,kitchen]]

currentFloor = firstFloor

while True:

    print(currentRoom.intro())
    if currentRoom.action != None:
        if currentRoom.secretItem != None:
            inventory.append(currentRoom.secretItem)
        currentRoom.doAction()
    print()
    currentRoom = moveRooms(currentRoom,currentFloor)
    if currentRoom.magicDoor != None:
        currentRoom.magicDoor.unlocked()
        if currentRoom.magicDoor.disabled


    print()
    print()