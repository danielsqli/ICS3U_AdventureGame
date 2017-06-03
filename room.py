import Secret
class Room:
    def __init__(self, name, description, exits, roomnumber, action, result):
        self.name = name
        self.description = description
        self.exits = exits
        self.roomNumber = roomnumber
        self.action = action
    def intro(self):
        return self.description
    def exitWays(self):
        print("There are exits to your " + ", ".join(self.exits[:len(self.exits)-1]) + " and " + str(self.exits[-1]))
        return input("Which Direction? ")
    def action(self):
        if self.action == None:
            return
        choice = input(self.action + "(y/n)")
        if choice == "y":
            return self.result
        else:
            return



