class Vehicle:
    def __init__(self, name, license_plate, color, speed, location, is_broken):
        self.name = name
        self.license_plate = license_plate
        self.color = color
        self.speed = speed
        self.location = location
        self.is_broken = is_broken
    
    def move(self, time):
        self.location += time * self.speed

    def honk(self):
        print('...')

    def check_status(self):
        if self.is_broken == False:
            print(self.name, ': good')
        else:
            print(self.name, ': broken')
    
class Car(Vehicle):
    def honk(self):
        print('Beep')

class Bicycle(Vehicle):
    def honk(self):
        print('Ring')

class Truck(Car):
    def __init__(self, name, license_plate, color, speed, location, is_broken, length):
        self.length = length
        super().__init__(name, license_plate, color, speed, location, is_broken)

    def honk(self):
        super().honk()
        print("Bop")

    def open_truck(self):
        print('Opening truck')

car1 = Car('Car01', 0000, 'red', 10, 0, False)
bicycle1 = Bicycle('Bicycle02', 1111, 'yellow', 5, 0, False)
truck1 = Truck('Truck03', 9999, 'blue', 15, 0, False)   

while car1.location < 100:
    car1.move(2)
    car1.honk()

bicycle1.location = 50
truck1.location = 0

while bicycle1.is_broken == False and car1.is_broken == False:
    bicycle1.move(1)
    truck1.move(1)

    bicycle1.check_status()
    truck1.check_status()

    if bicycle1.location == truck1.location:
        bicycle1.is_broken = True
        truck1.is_broken = True

bicycle1.check_status()
truck1.check_status()
