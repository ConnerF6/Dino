import random as ran

food = {
    "carnivore": ["bear", "cow", "deer", "mammoth", "chicken", "fish", "another dinosaur", "horses"],
    "herbivore": ["grass", "tree bark", "berries", "leaves", "fruit", "seeds", "lettuce"],
    "omnivore": ["bear", "cow", "deer", "mammoth", "chicken", "fish", "another dinosaur", "horses", "grass", "tree bark", "berries", "leaves", "fruit", "insects", "seeds", "lettuce"],
    "inedible": ["trash", "rotten meat", "anvil", "metal pan"]
    }

class Dinosaur(object):
    def __init__(self, name, species, diet, age, weight):
        self.name = name
        self.species = species
        self.diet = diet
        self.age = age
        self.weight = weight

    def dino_roar(self):
        return f"{self.name}: ROAARRRRRRRRRRRR"
    
    def give_dino_meal(self, meal):

        if meal in food[self.diet]:
            return f"{self.name} eats {meal}! Yum!"
        elif meal in food["inedible"]:
            return f"You didn't just try to feed {self.name} {meal}, did you? That's inedible!"
        else:
            return f"{self.name} doesn't seem to like {meal}!"
    
    def dino_eat(self):
        if self.diet == "herbivore":
            meal_choice = ran.choice(food["herbivore"])
            return f"{self.name} is going to be eating: \n{meal_choice}!"
        
        if self.diet == "carnivore":
            meal_choice = ran.choice(food["carnivore"])
            return f"{self.name} is going to be eating: \n{meal_choice}!"
        
        if self.diet == "omnivore":
            meal_choice = ran.choice(food["omnivore"])
            return f"{self.name} is going to be eating: \n{meal_choice}!"

    def dino_info(self):
        return f"{self.name} is a {self.age}-year-old {self.species} that weighs {self.weight} lbs and is a {self.diet}."

T_Rex = Dinosaur("Terry", "T-Rex", "carnivore", 26, 13200)
Bronto = Dinosaur("Benny", "Brontosaurus", "herbivore", 80, 33000)
Stego = Dinosaur("Spike", "Stegosaurus", "herbivore", 12, 5500)
Trike = Dinosaur("Tina", "Triceratops", "herbivore", 30, 14000)
Veloci = Dinosaur("Vicky", "Velociraptor", "carnivore", 7, 33)
Ankylo = Dinosaur("Andy", "Ankylosaurus", "herbivore", 16, 6000)
Spino = Dinosaur("Sparky", "Spinosaurus", "carnivore", 35, 15000)
Pachy = Dinosaur("Paul", "Pachycephalosaurus", "herbivore", 18, 2200)
Compy = Dinosaur("Charlie", "Compsognathus", "carnivore", 3, 15)
Iguano = Dinosaur("Iggy", "Iguanodon", "herbivore", 28, 9600)
Ptero = Dinosaur("Petra", "Pterodactyl", "omnivore", 22, 55)
Allo = Dinosaur("Alex", "Allosaurus", "carnivore", 27, 8400)

Dinosaurs = [T_Rex, Bronto, Stego, Trike, Veloci, Ankylo, Spino, Pachy, Compy, Iguano, Ptero, Allo]

for Dino in Dinosaurs:
    print(Dino.dino_info())
    print(Dino.dino_eat())
    print(Dino.dino_roar(), "\n")

print(T_Rex.give_dino_meal("bear"))
print(Bronto.give_dino_meal("grass"))
print(Ptero.give_dino_meal("seeds"))
print(T_Rex.give_dino_meal("trash"))
print(T_Rex.give_dino_meal("rotten meat"))