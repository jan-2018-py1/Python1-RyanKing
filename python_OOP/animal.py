class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "Health:", self.health
        return self

horse = Animal("Horse", 200)
horse.walk().walk().walk().run().run().display_health()
print "-----------------------------------"

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)

    def pet(self):
        self.health += 5
        return self

spike = Dog("Spike")
spike.walk().walk().walk().run().run().pet().display_health()
print "-----------------------------------"

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"
        return self

trogdor = Dragon("Trogdor")
trogdor.fly().display_health()
print "-----------------------------------"

animal2 = Animal("animal2", 100)
animal2.display_health()
# animal2.pet()  # doesn't work
# animal2.fly()  # doesn't work
print "-----------------------------------"

# spike.fly()    # doesn't work
