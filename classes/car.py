class Car:
    color: str
    model: str
    make: str

    def __init__(self, color, model, make):
        self.color = color
        self.model = model
        self.make = make

    def print(self):
        print("this is a " + self.make + " " + self.model)


car_one = Car("blue","optima","kia")
car_one.print()
