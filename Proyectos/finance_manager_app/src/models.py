#OOP classes
class Category():
    def __init__(self,name):
        self.name = name


class Movement():
    def __init__(self,movement_type,title,amount,category):
        self.movement_type = movement_type
        self.title = title
        self.amount = amount
        self.category = category
        pass



class Account():
    def __init__(self, movements = None, initial_balance = 0):
        if movements is None:
            movements = []
        self.movements = movements 
        self.balance = initial_balance 

        for m in movements:
            if m.movement_type == "expense":
                self.balance -= m.amount
            elif m.movement_type == "income":
                self.balance += m.amount

    def apply_movement(self,movement):
        if movement.movement_type == "expense":
            self.balance -= movement.amount
        elif movement.movement_type == "income":
            self.balance += movement.amount
        self.movements.append(movement)

