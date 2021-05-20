class Person:
    def __init__(self, firstname, lastname, health, status):
        "intialize attributes to be used in/available for all class methods in \
        this class, and for class objects created by this class . "

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "People must introduce themselves first"
        print("Hello my name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        "measuring the emotions of people"
