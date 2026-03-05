class Person():
    def __init__(self,name):
        self.name = name


class Bus():
    def __init__(self, max_passengers):
        self.max_passengers = int(max_passengers)
        self.passengers = []
    
    def add_passenger(self):
        if len(self.passengers) < self.max_passengers:
            passenger = Person(input("Enter the name of the passenger: "))
            self.passengers.append(passenger.name)
            return print(f"Now {passenger.name} is on board!")
        else:
            return print(f"The bus is full of passengers! This are the passengers: {self.passengers}")

new_bus = Bus(4)
new_bus.add_passenger()
new_bus.add_passenger()
new_bus.add_passenger()
new_bus.add_passenger()
new_bus.add_passenger()