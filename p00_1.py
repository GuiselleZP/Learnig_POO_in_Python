class Car():
    # Initial state
    def __init__(self):
        self.long_car = 250
        self.width  = 120
        # Encapsulated
        self.__wheels = 4
        self.__moving = False
    
    def move(self, it_move):
        self.moving = it_move
        if(self.moving):
            return "The car is moving"
        else:
            return "The car is stopped"

    def state(self):
        print("The car has {} wheels, has a width of {}cm and a lenght of {}cm"\
                .format(self.__wheels, self.width, self.long_car))
            
my_car = Car()
print(my_car.move(True))
my_car.state()

print('\nAnother car\n')

my_car2 = Car()
print(my_car2.move(False))
my_car2.__wheels = 5
my_car2.state()
