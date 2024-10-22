import random as ran

class Dinosaur(object):
    def __init__(self, name, species, diet, age, weight):
        self.name = name
        self.species = species
        self.diet = diet
        self.age = age
        self.weight = weight

    def dino_roar(self):
        return f"{self.name}: ROAARRRRRRRRRRRR"

    def dino_eat(self):
        if self.diet == "herbivore":
            meal_choice = ran.randint(1, 3)
            if meal_choice == 1:
                return f"{self.name} is going to be eating: \nLeaves from a Willow tree!"
            elif meal_choice == 2:
                return f"{self.name} is going to be eating: \nDifferent kinds of fruit!"
            elif meal_choice == 3:
                return f"{self.name} is going to be eating: \nLettuce!"
        
        if self.diet == "carnivore":
            meal_choice = ran.randint(1, 3)
            if meal_choice == 1:
                return f"{self.name} is going to be eating: \na Bear!"
            elif meal_choice == 2:
                return f"{self.name} is going to be eating: \nAnother dinosaur!"
            elif meal_choice == 3:
                return f"{self.name} is going to be eating: \nHorses!"
        
        if self.diet == "omnivore":
            meal_choice = ran.randint(1, 3)
            if meal_choice == 1:
                return f"{self.name} is going to be eating: \nLeaves from a Willow tree and a Bear!"
            elif meal_choice == 2:
                return f"{self.name} is going to be eating: \nDifferent kinds of fruit and another dinosaur!"
            elif meal_choice == 3:
                return f"{self.name} is going to be eating: \nLettuce and Horses!"

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