#Dushyant Tara(22-06-2020):This program helps you understand unit tests in python

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name.

    Args:
        first (str): First name of the user
        last (str): Last name of the user
        middle (str, optional): Middle name of the user. Defaults to ''.

    Returns:
        str: Formatted Full name
    """
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
        
    return full_name.title()

