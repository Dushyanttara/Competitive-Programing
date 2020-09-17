#Dushyant Tara(21-06-2020): This program helps you understand 
#-inheritence in classes
#-Defining attributes and methods for the child class
#-Overriding methods from the parent class
#-Instances as attributes
from car import Car

class Battery():
    """A simple attempt to model a battery for an electric car.
    """

    def __init__(self,battery_size = 70):
        """Initialize the battery's attributes.

        Args:
            battery_size (int, optional): Size of the batter in kWh. Defaults to 70.
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size.
        """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides.
        """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)        
    
    def upgrade_battery(self):
        """Upgrades the battery if it is of a lower grade
        """
        if self.battery_size != 85:
            print("upgrading your car....")
            self.battery_size = 85

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles.

    Args:
        Car (Class): Class respresenting a simple car
    """
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.

        Args:
            make (str): Manufacturer of the car
            model (str): Model of the car
            year (int): year of purchase    
        """        
        super().__init__(make, model, year)
        self.battery = Battery()
    
    #overriding method from car class(in case car class had a method named fill_gas_tank)
    def fill_gas_tank(self):
        """Electric cars don't have a gas tanks.
        """
        print("This car doesn't need a gas tank!")            


