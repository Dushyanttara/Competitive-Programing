#Dushyant Tara(20-06-2020):This program helps you understand functions and returns
def get_formatted_name(first_name ,last_name):
    """Return a full name, neatly formated."""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

#Making an argument optional
def get_formatted_name(first_name ,last_name,middle_name =''):
    """Return a full name, neatly formated."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jhony','hendrix1',middle_name='Ramos')
print(musician)