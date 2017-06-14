class MagicDoor:
    def __init__(self, key, ghost):
        self.disabled = False
        self.key = key
        self.ghost = ghost
    def unlocked(self,inventory):
        if type(self.key) == list:
            keysOwned = 0
            for i in self.key:
                if i in inventory:
                    keysOwned += 1
            if keysOwned == len(self.key):
                return True
            else:
                return False
        else:
            if self.key in inventory:
                print("Used the " + self.key.name + ". It opened the door")
                return True
            else:
                return False