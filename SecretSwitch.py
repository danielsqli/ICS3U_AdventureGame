class SecretSwitch:
    def __init__(self, name, function, activatemethod):
        self.name = name
        self.function = function
        self.activateMethod = activatemethod
    def discovery(self):
        print("You found a secret" + self.name)
        activate = input(self.activateMethod + "the" + self.name + "? (y/n)")

        while activate.lower() not in ["y","yes","n","no"]:
            activate = input(self.activateMethod + "the" + self.name + "? (y/n)")

        if activate.lower() == "y" or activate.lower == "yes":
            choice = input(self.name + "opened a secret passage. Enter? (y/n)")

            while choice.lower() not in ["y", "yes", "n","no"]:
                choice = input(self.activateMethod + "the" + self.name + "? (y/n)")

            if choice.lower() == "y" or activate.lower == "yes":
                return True