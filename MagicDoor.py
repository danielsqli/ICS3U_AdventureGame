class MagicDoor:
    def __init__(self, key, ghost):
        self.disabled = False
        self.key = key
        self.ghost = ghost
    def unlocked(self,inventory):
        if self.key in inventory:
            return True
        else:
            return False