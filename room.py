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
        """
        Introducing the room
        :return: str - the introduction
        """
        return self.description
    def exitWays(self):
        """
        Getting a direction to leave the room
        :return: str - direction
        """
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
        """
        Doing something in the room
        :param inventory: inventory of items
        :returns: bool - True if ghost attack, str - "win" if you won, str - "save" if choice is to save
                 None - if choice is nothing or a useless action is chosen, str - "switch" if a switch is found
                 int - index of item found if more than 1 item in room,
        """
        # Checking if all useful actions have been completed
        if self.completed == False:

            # Checking if action is 'win'
            if self.action[0] == 'win':
                # return "win" if so
                return "win"
            print("What to do?")

            # Getting a numerical choice for the action
            for i in range(len(self.action)):
                print("{0}. {1}".format(i+1,self.action[i]))
            while True:
                try:
                    choice = int(input("Enter number of the choice: "))
                    break
                except ValueError:
                    print("That is not valid")

            # Checking if choice is save
            if choice == 10:
                return "Save"

            # Checking if result of choice is Nothing
            elif self.result[choice-1] == "Nothing":
                return

            # Checking if result of choice is a ghost attack
            elif self.result[choice-1] == "GHOST ATTACK":
                return "GHOST ATTACK"

            # Checking if the result of choice is an item
            elif type(self.result[choice-1]) == int:
                itemsGathered = 0
                result = self.result[choice-1]

                # Checking if more than 1 item in room
                if type(self.secretItem) == list:

                    # Using a loop to check if all the items have been collected
                    for i in range(len(self.secretItem)):
                        if self.secretItem[i] in inventory:
                            itemsGathered += 1

                        # Return "switch" if secret item is a secret switch
                        if self.secretItem[i].type == "Switch":
                            return "switch"
                    if itemsGathered == len(self.secretItem):
                        # If all items have been gathered, mark room as completed
                        self.completed = True

                # Else if only 1 item
                else:
                    # Mark room as completed
                    self.completed = True

                    # Return "switch is secret item is a secret switch
                    if self.secretItem.type == "Switch":
                        return "switch"

                # Removing the choice to grab the item again
                self.action.remove(self.action[choice - 1])
                self.result.remove(self.result[choice - 1])
                return result

            # If action does nothing, print the result and removing the choice
            else:
                print(self.result[choice-1])
                self.action.remove(self.action[choice-1])
                self.result.remove(self.result[choice-1])

    def locked(self, inventory):
        """
        Checking if a room is locked
        :param inventory: inventory of items
        :return: bool - True if locked, False if unlocked
        """
        # Checking if the door is locked
        if self.magicDoor.unlocked(inventory) == True:
            self.magicDoor.disabled = True

        # Return true or false based on that
        if self.magicDoor.disabled == True:
            return False
        else:
            return True

# Sub class of rooms for stairs
class Stairs(Room):

    def exitWays(self):
        """
        Finding a direction to go
        :return: str - direction
        """
        # Checking if you can go both directions
        if len(self.exits) > 1:
            direction = input("Up or down?")

            # Retrieve a value for direction
            while direction.lower() not in ["up", "down"]:
                direction = input("Not valid, up or down?")

        # If only 1 direction
        else:
            direction = input('You can go ' + self.exits[0])

            # Get direction
            while direction.lower() != self.exits[0]:
                direction = input("Not valid, " + self.exits[0])
        print("Going " + direction)

        # Return direction
        return direction


