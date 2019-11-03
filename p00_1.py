class Car():
    # Initial state
    def __init__(self):
        self.__long_car = 250
        self.__width = 120
        self.__wheels = 4
        self.__moving = False

    def move(self, it_move):
        self.__moving = it_move
        if(self.__moving):
            review = self.__internal_review()
        if(self.__moving and review):
            return "The car is moving"
        if(self.__moving and review is False):
            return "Something has failed in the review, the car cannot start"
        else:
            return "The car is stopped"

    def state(self):
        print("The car has {} wheels, has a width of {}cm and a lenght of {}cm"
              .format(self.__wheels, self.__width, self.__long_car))

    def __internal_review(self):
        print('Performing internal review')
        self.oil = "ok"
        self.gasoline = "failed"
        self.doors = "closed"
        if(self.gasoline == "ok" and self.oil == "ok" and self.doors ==
           "closed"):
            return True
        else:
            return False


my_car = Car()
print(my_car.move(True))
my_car.state()
print('\nAnother car\n')
my_car2 = Car()
print(my_car2.move(False))
