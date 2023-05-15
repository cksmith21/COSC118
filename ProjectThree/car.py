class Car(): 

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        print(f'The car\'s sped is {self.__speed}.')

if __name__ == "__main__": 

    car = Car("2012 Accord", "Honda")

    print("The car is accelerating...")
    for i in range(5):
        car.accelerate()
        car.get_speed() 

    print("The car is breaking...")
    for i in range(5): 
        car.brake()
        car.get_speed() 