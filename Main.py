import room
import SecretObject

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
hallway = room.Room("hallway", "You are in a dimly lit hallway", ["north","west","n","w"], "There is a light switch. Turn on the lights?", "You can now see better",None)
closet = room.Room("closet", "You are in a musty closet with 2 jackets in it", ["north", "east","e", "n"], "Ruffle through the clothes?", "Already found key", key1)
hallway2 = room.Room("hallway","You are in a long hall lit by small lights",["west","north","east","south","w","n","e","s"], None, None, None)
currentRoom = hallway
inventory = []
firstFloor = [[0,1,2,None],[None,hallway2,5,6],[closet,hallway,9,10]]

currentFloor = firstFloor

while True:

    print(currentRoom.intro())
    if currentRoom.action != None:
        if currentRoom.secretItem != None:
            inventory.append(currentRoom.secretItem)
        currentRoom.doAction()
    print()
    currentRoom = moveRooms(currentRoom,currentFloor)

    print()
    print()