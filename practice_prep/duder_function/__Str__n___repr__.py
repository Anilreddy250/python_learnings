class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self. year = year
    
    # def __str__(self):
    #     return f"{self.year} {self.make}{self.model}"
    def __str__(self):
        return f"Car(make = '{self.make}, model = '{self.model},year= '{self.year}')"
my_Car = Car("Toyota", "corolla", 2021)
#calling__str__
print(my_Car)
# print(repr(my_Car))