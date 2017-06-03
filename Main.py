import room
import Secret
firstFloor = [[0,1,2,None],[None,4,5,6],[7,8,9,10]]
hallway = room.Room("hallway", "You are in a dimly lit hallway", ["north","west","east"], 8, None, None)

print(hallway.intro())
print(hallway.exitWays())