#Dushyant Tara(23-06-2020):This program helps us understand how to use unit testing in python

class Employee():
    """A simple class to represent an employee.
    """
    def __init__(self,first,last,salary):    
        """Initializes the Employee class.

        Args:
            first (str): First name of the employee
            last (str): Last name of the employee
            salary (int): Annual Salary of the Employee
        """
        self.first_name = first
        self.last_name = last 
        self.salary = salary 

    def give_raise(self,raise_salary=5000):
        """Raises the annual salary by the given amount

        Args:
            raise (int, optional): Raise amount. Defaults to 5000.
        """
        self.salary += raise_salary

