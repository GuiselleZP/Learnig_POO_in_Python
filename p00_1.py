class Car():
    long_car = 250
    width  = 120
    wheels = 4
    moving = False
    
    def move(self):
        self.moving = True

    def state(self):
        if self.moving:
            return "The car is moving"
        else:
            return "The car is stopped"

my_car = Car()
print(my_car.state())
my_car.move()
print(my_car.state())
