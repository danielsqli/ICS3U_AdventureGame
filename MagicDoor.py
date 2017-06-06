class MagicDoor:
    def __init__(self, key):
        self.disabled = False
        self.key = key
    def unlocked(self):
        if self.key:
            self.disabled = True
