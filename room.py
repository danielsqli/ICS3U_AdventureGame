import SecretSwitch
import MagicDoor
class Room:
    def __init__(self, name, description, exits , action, result, secretitem, magicdoor, type="Room", checkpoint=False):
        self.name = name
        self.description = description
        self.exits = exits
        self.action = action
        self.result = result
        self.secretItem = secretitem
        self.completed = False
        self.type = type
        self.magicDoor = magicdoor
        self.checkPoint = checkpoint
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
    def doAction(self,inventory):
        if self.completed == False:
            if self.action is None:
                return "win"
            print("What to do?")
            for i in range(len(self.action)):
                print("{0}. {1}".format(i+1,self.action[i]))
            while True:
                try:
                    choice = int(input("Enter number of the choice: "))
                    break
                except ValueError:
                    print("That is not valid")
            if choice == 10:
                return "Save"
            elif self.result[choice-1] == "Nothing":
                return
            elif self.result[choice-1] == "GHOST ATTACK":
                return True
            elif type(self.result[choice-1]) == int:
                itemsGathered = 0
                if type(self.secretItem) == list:
                    for i in range(len(self.secretItem)):
                        if self.secretItem[i] in inventory:
                            itemsGathered += 1
                        if self.secretItem[i].type == "Switch":
                            return "switch"
                    if itemsGathered == len(self.secretItem):
                        self.completed = True

                else:
                    self.completed = True
                    if self.secretItem.type == "Switch":
                        return "switch"



                result = self.result[choice-1]
                self.action.remove(self.action[choice - 1])
                self.result.remove(self.result[choice - 1])
                return result

            else:
                print(self.result[choice-1])
                self.action.remove(self.action[choice-1])
                self.result.remove(self.result[choice-1])

    def locked(self, inventory):
        if self.magicDoor.unlocked(inventory) == True:
            self.magicDoor.disabled = True
        if self.magicDoor.disabled == True:
            return False
        else:
            return True


class Stairs(Room):
    def exitWays(self):
        if len(self.exits) > 1:
            direction = input("Up or down?")
            while direction.lower() not in ["up", "down"]:
                direction = input("Not valid, up or down?")
        else:
            direction = input('You can go ' + self.exits[0])
            while direction.lower() != self.exits[0]:
                direction = input("Not valid, " + self.exits[0])
        print("Going " + direction)

        return direction


