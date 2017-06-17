class SecretObject:
    def __init__(self, name, function, discovery,type="Object"):
        self.name = name
        self.function = function
        self.discovery = discovery
        self.type = type
    def __repr__(self):
        """
        Printing the discovery of item
        :return: str - discovery phrase
        """
        return "Found a " + self.name + " that " + self.discovery + ". It " + self.function
