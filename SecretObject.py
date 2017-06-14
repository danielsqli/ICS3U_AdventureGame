class SecretObject:
    def __init__(self, name, function, discovery):
        self.name = name
        self.function = function
        self.discovery = discovery
    def __repr__(self):
        return "Found a " + self.name + " that " + self.discovery + ". It " + self.function


