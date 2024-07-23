class Ninja:
def __init__(self, first_name, last_name, treats, pet_food, pet):
    self.first_name = first_name
    self.last_name = last_name
    self.pet = pet
    self.treats = treats
    self.pet_food = pet_food

def walk(self):
        self.pet.play()
        print(f"{self.first_name} {self.last_name} is walking their pet!")

def feed(self):
    self.pet.eat()
    print(f"{self.first_name} {self.last_name} is feeding their pet!")

def bathe(self):
    self.pet.noise()
    print(f"{self.first_name} {self.last_name} is bathing their pet!")
#--------------------------NINJA-------------------------------------------------
    class Pet:
def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50

def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping... Zzz...")

def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating... Om nom nom...")

def play(self):
        self.health += 5
        print(f"{self.name} is playing... Woohoo!")

def noise(self):
        if self.type == "dog":
            print("Woof!")
        elif self.type == "cat":
            print("Meow!")
        else:
            print("Unknown pet sound...")
#--------------------------------pet----------------------------------------------
