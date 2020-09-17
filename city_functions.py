#Dushyant Tara(23-06-2020):This program helps you understand unit testing in python

def city_country(city,country,population = ''):
    """Returns formatted city country with population

    Args:
        city (str): Name of city
        country (str): Name of country
        population (int, optional): Population of the city. Defaults to ''.

    Returns:
        str: Formatted city,country
    """    
    if population:
        city_country = city.title() + ', ' + country.title() + ' - population ' + str(population)
    else:
        city_country = city.title() + ', ' + country.title()
    return city_country

