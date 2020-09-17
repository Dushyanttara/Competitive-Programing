from user_profile import User
        
#New class Priveleges for adding all priveleges
class Priveleges():
    """A simple attempt to create a class for all priveleges.
    """
    def __init__(self, priveleges= ['can add user','can delete user']):
        """Initializes the Priveleges class

        Args:
            priveleges (list, optional): List of priveleges for a user type. Defaults to ['can add user','can delete user'].
        """ 
        self.priveleges = priveleges

    def show_priveleges(self):
        """Prints all the priveleges for a given user.
        """
        print("Priveleges: ")
        for privelege in self.priveleges:
            print("\t-" + privelege)                
            
#New class admin to be created for permissions
class Admin(User):
    """A simple attempt to create and Admin profile

    Args:
        User (class): User class earlier created
    """
    def __init__(self, first_name, last_name, **userinfo):
        """Initialize the parent User class 
           Then sets attributes for the child class Admin

        Args:
            first_name (str): First name of Admin
            last_name (str): Last name of Admin
        """        
        super().__init__(first_name, last_name, **userinfo)
        self.priveleges = Priveleges()
