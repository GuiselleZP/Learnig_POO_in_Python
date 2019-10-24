class Vehicles():
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model
        self.moving = False
        self.speeding_up = False
        self.stopping = False

    def start(self):
        self.moving = True

    def speed_up(self):
        self.speeding_up = True

    def stop(self):
        self.stopping = True

    def state(self):
        print("Mark: {}\nModel: {}\nMoving: {}\nSpeeding_up: {}\nStopping: {}"\
                .format(self.mark, self.model, self.moving, self.speeding_up,\
                self.stopping))
    
class Van(Vehicles):
    def load(self, loading):
        self.loading = loading
        if(self.loading):
            return "The van is loaded"
        else:
            return "The van is not loaded"

class Motorcycle(Vehicles):
    wheelie = ''
    def doing_wheelie(self):
        self.wheelie = "I am doing wheelie. "
    def state(self):
        print("Mark: {}\nModel: {}\nMoving: {}\nSpeeding_up: {}\nStopping: {}\
                \nWheelie: {}"  .format(self.mark, self.model, self.moving, \
                self.speeding_up, self.stopping, self.wheelie))

class ElectricVehicle():
    def __init__(self):
        self.autonomy = 100

    def charge_power(self):
        self.charging = True
    
class ElectricBicycle(ElectricVehicle, Vehicles):
    pass

my_Motorcycle = Motorcycle("Honda", "CBR")
my_Motorcycle.doing_wheelie()
my_Motorcycle.state()

my_van = Van("Renault", "Kangoo")
my_van.start()
my_van.state()
my_van.load(True)

my_bicycle = ElectricVehicle()
