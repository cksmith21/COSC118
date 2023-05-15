class Pet(): 
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age 

    def change_name(self, n_name):
        self.name = n_name
    
    def change_age(self, n_age):
        self.age = n_age

    def get_name(self):
        print(f'The animal\'s name is {self.name}.')

    def get_animal_type(self):
        print(f'The animal\'s type is {self.animal_type}.')

    def get_age(self):
        print(f'The animal\'s age is {self.age}.')

if __name__ == "__main__":

    name = input("Enter the pet's name: ")
    age = int(input("Enter the pet's age: "))
    type = input("Enter the animal's type: ")

    new_pet = Pet(name, type, age)

    new_pet.get_name()
    new_pet.get_animal_type()
    new_pet.get_age()