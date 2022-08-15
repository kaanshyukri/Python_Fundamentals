class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, type):
        if species == "mammal":
            self.mammals.append(type)
        elif species == "fish":
            self.fishes.append(type)
        elif species == "bird":
            self.birds.append(type)

        Zoo.__animals += 1

    def get_info(self, species):
        res = ""
        if species == "mammal":
            res += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            res += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            res += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        res += f"Total animals: {Zoo.__animals}"
        return res


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_animals = int(input())

for _ in range(number_of_animals):
    animals = input().split()
    type_of = animals[0]
    animal = animals[1]
    zoo.add_animal(type_of, animal)

name = input()
print(zoo.get_info(name))
