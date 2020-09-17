#Dushyant Tara(21-06-2020):This program helps you import classes from modules
from car import Car, ElectricCar
#or import the whole module using
#import car then use car.Car or car.ElectricCar syntax

my_beetle = Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())
