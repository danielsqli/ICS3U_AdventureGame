class MagicDoor:
    def __init__(self, key, ghost):
        self.disabled = False
        self.key = key
        self.ghost = ghost
    def unlocked(self,inventory):
        """
        Checking if door is unlocked
        :param inventory: inventory of items
        :return: bool - True if unlocked, False if locked
        """
        # Check if mulitply keys for the 1 door
        if type(self.key) == list:
            keysOwned = 0

            # If so, checks if all the keys are present
            for i in self.key:
                if i in inventory:
                    keysOwned += 1

            # Return true if all keys are there, otherwise, false
            if keysOwned == len(self.key):
                return True
            else:
                return False

        # If only 1 key
        else:
            # Check if key is in inventory and returns True if so, otherise, False
            if self.key in inventory:
                print("Used the " + self.key.name + ". It opened the door")
                return True
            else:
                return False