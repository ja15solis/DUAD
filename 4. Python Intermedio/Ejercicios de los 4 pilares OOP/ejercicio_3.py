#Multiple Inheritance
#kwargs stops takes all the remaining arguments and creates a dictionary with it and the ** is unpacking it

#Structure: It turns arguments into a dictionary.
#Flexibility: It allows functions to handle arguments they didn't know they were going to receive.
#Cleanliness: It prevents you from having to rewrite long lists of arguments in every subclass.

class Motor:
    def __init__(self, **kwargs): #motor doesn't needs the battery or fuel but still accept kwargs 
        super().__init__()

    def start_engine(self):
        return "The engine has started"
    
    def turn_of_engine(self):
        return "The engine has been turn off"

class CombustionMotor(Motor):
    def __init__(self,fuel,fuel_efficiency,**kwargs): #takes fuel and fuel efficiency and pass the rest to motor
        super().__init__(**kwargs)
        self.fuel = fuel
        self.fuel_efficiency = fuel_efficiency

class ElectricMotor(Motor):
    def __init__(self,battery,battery_efficiency,**kwargs): #takes battery and battery efficiency and pass the rest to combustion motor
        super().__init__(**kwargs)
        self.battery = battery
        self.battery_efficiency = battery_efficiency

class HybridCar(ElectricMotor,CombustionMotor): #first creates the electric motor
    def __init__(self,battery,battery_efficiency,fuel,fuel_efficiency):
        super().__init__(
            battery=battery, 
            battery_efficiency=battery_efficiency, 
            fuel=fuel, 
            fuel_efficiency=fuel_efficiency
        )

    def driving(self):
        return f"The car is using a electric motor with a {self.battery} with a efficiency of {self.battery_efficiency}% and also a combustion motor, using {self.fuel} with efficiency of {self.fuel_efficiency}%"

car = HybridCar("Lithium",80,"Gasoline Plus", 40)
#first creates the electric motor
#takes battery and battery efficiency to create "ElectricMotor" and pass the rest to combustion motor
#takes fuel and fuel efficiency to create "CombustionMotor" and pass the rest to motor
#creates motor and stop the chain

print(car.start_engine())
print(car.driving())
print(car.turn_of_engine())