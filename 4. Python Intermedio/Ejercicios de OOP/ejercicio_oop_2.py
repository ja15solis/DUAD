class Person():
    def __init__(self,name):
        self.name = name
        pass
    


class Bus():
    def __init__(self, max_passengers):
        self.max_passengers = int(max_passengers)
        self.passengers_on_board = 0
        pass
    
    def add_passenger(self):
        while self.passengers_on_board < self.max_passengers:
            Person(input("Please enter the name of the passenger: "))
            self.passengers_on_board += 1
        print("The bus is full of passengers!")

new_bus = Bus(4)
new_bus.add_passenger()