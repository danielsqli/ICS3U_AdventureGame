import Main
class MagicDoor:
    def __init__(self, key):
        self.disabled = False
        self.key = key
    def unlocked(self):
        if self.key in Main.inventory:
            return True
        else:
            return False