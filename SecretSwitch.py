class SecretSwitch:
    def __init__(self, name, roomsChanged,result, activated=False,type="Switch"):
        self.name = name
        self.roomsChanged = roomsChanged
        self.activated = activated
        self.result = result
        self.type = type
    def discovery(self):
        print("You found a secret " + self.name)
        print("You flipped the switch")
        print(self.result)
    def action(self,houseMap):
        for i in houseMap:
            for j in range(len(i)):
                for k in range(len(i[j])):
                    if i[j][k] == self.roomsChanged[0]:
                        i[j][k] = self.roomsChanged[1]
                        return houseMap