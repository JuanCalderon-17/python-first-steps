
class Vehicle:
    def __init__(self, max_speed, mileage):  
        self.max_speed = max_speed
        self.mileage = mileage

    def printing_speed_Vehicle(self):
        print("We see this is correct")
    
class Bus(Vehicle):
    def printing_speed_car(self):
        print("def this is correct")
        

roll_royce = Vehicle(200, 5000)
roll_royce.printing_speed_Vehicle()

bmw = Bus(180, 6000)
bmw.printing_speed_car()

print(roll_royce.max_speed, roll_royce.mileage)
