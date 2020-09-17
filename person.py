#Dushyant Tara(20-06-2020): This program helps you understand to return dictionaries through a function

def build_person(first_name,last_name):
    """This function returns a dictionary of information about a person

    Args:
        first_name (string): first name of the person
        last_name (string): last name of the person
    """    
    person = {'first':first_name, 'last':last_name}
    return person

music = build_person('mark','saddler')
print(music)

def build_person(first_name,last_name,age=''):
    """Return a dictionary of information about a person.

    Args:
        first_name (str): first name of the person
        last_name (str): last name of the person
        age (int, optional): age of the person. Defaults to ''.
    """    
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',age=25)
print(musician)