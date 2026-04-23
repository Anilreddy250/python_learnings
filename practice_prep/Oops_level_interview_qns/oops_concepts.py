#class @Object
class Motorcycle:
    def __init__(self, brand, model):
        self.brand =brand
        self.model = model
    def start_engine(self):
        print(f"the {self.brand}{self.model}engine is idling...")
my_bike = Motorcycle("Husqvarna","svartpilen_250")
my_bike.start_engine()

    
#Inhertance:
class AdevntureBike(Motorcycle):
    def __init__ (self, brand, model, ground_clearance):
        super().__init__(brand, model) #inherit brand and model
        self.ground_clearance = ground_clearance
    def go_offroad(self):
        print(f"Navigating rocks with {self.ground_clearance}mm clearance")

adv_bike = AdevntureBike("Ktm","390 Adventure", 200)
adv_bike.start_engine() #inherited mothond
adv_bike.go_offroad() #Specific method


#encapsulation:
class Dashboard:
    def __init__(self):
        self.__odometer = 5000 #privete attribute
    def drive(self,kms):
        if kms > 0:
            self.__odometer += kms
            print(f"Odometer Updated : {self.__odometer}km")
    def get_reading(self):
        return self.__odometer
my_dash = Dashboard()
my_dash.drive(150)

#Polymorphism:
class Svartpilen:
    def exhaust_note(self):
        return "crisp Thump"
class Himalayan:
    def exhaust_note(self):
        return "Deep grumble"
def play_sound(bike_obj):
    print(bike_obj.exhaust_note())
play_sound(Svartpilen())
play_sound(Himalayan())

#abstraction:
from abc import ABC, abstractmethod
class BrakingSystem(ABC):
    @abstractmethod
    def apply_brake(self):
        pass
class DiscBrake(BrakingSystem):
    def apply_brake(self):
        print("Applying hyfralic pressure to calipers")
class DrumBrake(BrakingSystem):
    def apply_brake(self):
        print("Expanding brake shoes against the drum.")
# my_brake = BrakingSystem() # This would raise an error (cannot instantiate abstract class)
front_brake = DiscBrake()
front_brake.apply_brake()