class MagicDoor:
    def __init__(self, key):
        self.disabled = False
        self.key = key
    def unlocked(self,inventory):
        if self.key in inventory:
            return True
        else:
            return False