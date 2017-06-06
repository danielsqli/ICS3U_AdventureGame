import SecretSwitch
class Room:
    def __init__(self, name, description, exits , action, result, secretitem):
        self.name = name
        self.description = description
        self.exits = exits
        self.action = action
        self.result = result
        self.secretItem = secretitem
        self.completed = False
    def intro(self):
        return self.description
    def exitWays(self):
        print("There are exits to your " + ", ".join(self.exits[:len(self.exits)//2 -1]) + " and " + str(self.exits[len(self.exits)//2-1]))
        direction = input("Which direction ")
        while direction.lower() not in self.exits:
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



