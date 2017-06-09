import SecretSwitch
class Room:
    def __init__(self, name, description, exits , action, result, secretitem, type="Room"):
        self.name = name
        self.description = description
        self.exits = exits
        self.action = action
        self.result = result
        self.secretItem = secretitem
        self.completed = False
        self.type = type
    def intro(self):
        return self.description
    def exitWays(self):
        if len(self.exits) > 1:
            print("There are exits to your " + ", ".join(self.exits[:len(self.exits)-1]) + " and " + str(self.exits[-1]))
        else:
            print("There is an exit to your",str(self.exits[0]))
        direction = input("Which direction ")
        while direction.lower() not in self.exits and direction.lower() not in "".join([x[0] for x in self.exits]):
            print("Can't go that way")
            direction = input("Which direction ")

        return direction
    def doAction(self):
        if self.completed == False:
            choice = input(self.action + "(y/n)")
            if choice == "y":
                if self.secretItem != None:
                    print("You found a",self.secretItem.name)
                else:
                    print(self.result)
        self.completed = True

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


