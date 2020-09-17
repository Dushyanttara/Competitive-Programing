#Dushyant Tara(20-06-2020): This program helps you understand how to pass list to a function

def greet_users(names):
    """Greet all users in a list

    Args:
        names (list): List containing usernames
    """    
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah','ty', 'margot']
greet_users(usernames)