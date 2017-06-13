import SecretSwitch
import MagicDoor
class Room:
    def __init__(self, name, description, exits , action, result, secretitem, magicdoor, type="Room"):
        self.name = name
        self.description = description
        self.exits = exits
        self.action = action
        self.result = result
        self.secretItem = secretitem
        self.completed = False
        self.type = type
        self.magicDoor = magicdoor
    def intro(self):
        return self.description
    def exitWays(self):
        if len(self.exits) > 1:
            print("There are exits to your " + ", ".join(self.exits[:len(self.exits)-1]) + " and " + str(self.exits[-1]))
        else:
            print("There is an exit to your",str(self.exits[0]))
        direction = input("Which direction ")
        while (direction.lower() not in self.exits and direction.lower() not in "".join([x[0] for x in self.exits])) or len(direction) < 1:
            print("Can't go that way")
            direction = input("Which direction ")

        return direction
    def doAction(self):
        if self.completed == False:
            print("What to do?")
            for i in range(len(self.action)):
                print("{0}. {1}".format(i+1,self.action[i]))
            choice = int(input("Enter number of the choice: "))
            if self.action[choice-1] == "Nothing":
                return
            elif self.action[choice-1] == "GHOST ATTACK":
                print("GHOST ATTACK")
            elif self.secretItem != None:
                print("You found a",self.secretItem.name)
                print("The",self.secretItem.name,self.secretItem.function)
                self.completed = True
            else:
                print(self.result[choice-1])
                self.completed = True
    def locked(self, inventory):
        if self.magicDoor.unlocked(inventory) == True:
            self.magicDoor.disabled == True
        if self.magicDoor.disabled == True:
            return False
        else:
            return True


class Stairs(Room):
    def exitWays(self):
        if len(self.exits) > 1:
            direction = input("Up or down?")
        else:
            direction = input('You can go ' + self.exits[0])
        while direction.lower() not in ("up", "down"):
            direction = input("Not valid, up or down?")
        print("Going " + direction)

        return direction


