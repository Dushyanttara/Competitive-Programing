#Dushyant Tara(20-06-2020):This program helps you understand how to work with classes.
class Dog():
    """A simple attempt to model a dog.
    """
    def __init__(self,name, age):
        """Initializes name and age attributes.

        Args:
            name (str): Name of the dog
            age (int): Age of the dog
        """
        self.name = name
        self.age = age

    def sit(self):
        """Simulates a dog sittingin response to a command.
        """
        print(self.name.title() + " is now sitting")                

    def roll_over(self):
        """Simulates rolling over in response to a command.
        """
        print(self.name.title() + " rolled over!")
                

#Making an instane from a class
my_dog = Dog('willie',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#calling methods
my_dog.sit()
my_dog.roll_over()


#Creating multiple instances
your_dog = Dog('lucy', 3)

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()