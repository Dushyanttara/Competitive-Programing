"""A class that can be used to represent a car.

Returns:
    class: A car class which can be imported to other files
"""
#Dushyant Tara(21-06-2020): This program helps you understand how to work with classes
#setting a default value for an attribute
#modifying attribute values
class Car():
    """A simple attempt to represent a car.
    """

    def __init__(self,make,model,year):    
        """Initialize attributes to describe a car.

        Args:
            make (str): Manufacturer of the car
            model (str): Model of the car
            year (int): Year of purchase
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name.
        """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage.
        """
        print("This car has " + str(self.odometer_reading) + " miles on it.")   

    #Modifying an attribute's value through a method
    def update_odometer(self,mileage):
        """Set the odometer reading to the given value.
            Reject the change if it attempts to roll the odometer back.

        Args:
            mileage (int): Miles the car has driven
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Warning: You can't roll back an odometer!")
    #Modifying an attribute value by incrementing through a method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading.

        Args:
            miles (int): Miles the car has driven after last time
        """
        self.odometer_reading += miles
            

#Dushyant Tara(21-06-2020): This program helps you understand 
#-inheritence in classes
#-Defining attributes and methods for the child class
#-Overriding methods from the parent class
#-Instances as attributes

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

"""my_new_car = Car('audi','a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(24)#using the update through the method
#modifying an attribute's value directly
#my_new_car.odometer_reading = 20
my_new_car.update_odometer(15)#using the update through the method
my_new_car.read_odometer()

my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()"""