class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = 100
        self.pet = pet

    def walk(self, pet):
        self.pet.play()
        return self

    def feed(self):
        amount = 10
        if (self.pet_food - amount) > 0:
            self.pet_food -= amount
            print(f"still have food! {self.pet_food}% left!")
        else: 
            print("going to the store, getting more food")
            self.pet_food = 100
        return self

    def bathe(self):
        self.pets.noise()


class Pet:
    def __init__(self, name, pet_type, tricks):
        self.name = name
        self.type = pet_type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
        self.noise = ""

    def sleep(self, name, energy):
        self.energy += 25
        return self

    def eat(self, health, energy):
        self.energy += 5
        self.health += 10
        return self

    def play(self, name, health):
        self.health += 5
        return self

    def noise(self):
        print("bark! bark!")
        return self



owner = Ninja("Cameron", "Bowen", "scooby doo snacks", 100, "Bentley")
print(owner.first_name)

bentley = Pet("Bentley", "American Bully", "sit")
print(bentley.name)


owner.feed()
owner.feed()
owner.feed()
owner.feed()
owner.feed()
owner.feed()
owner.feed()
owner.feed()
owner.feed()
owner.feed()
owner.feed()
owner.feed()

