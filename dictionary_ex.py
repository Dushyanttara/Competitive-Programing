#Dushyant Tara(19-06-2020):This program helps you understand nesting in dictionaries with examples
#People


vyom = {
    'first': 'vyom',
    'last' : 'bhatt',
    'university' : 'manipal',
}
sidhant = {
    'first': 'sidhant',
    'last' : 'gupta',
    'university' : 'bits',

}
shantanu = {
    'first' : 'shantanu',
    'last' : 'sharma',
    'university' : 'bits',
}

people = [vyom,sidhant,shantanu]

for individual in people:
    print(individual)


#Pets
evie = {
    'name':'evie',
    'kind':'dog',
    'breed':'shipooh',
    'owner':'sonal',
}

chui = {
    'name':'chui',
    'kind':'dog',
    'breed':'shih tzu',
    'owner' : 'tarun',
}

echo = {
    'name':'echo',
    'kind':'dog',
    'breed':'german shephard',
    'owner': 'nidhi',
}

pets = [evie,chui,echo]

for pet in pets:
    print(pet)

#Favorite places
favorite_places = {
    'Ram':['italy', 'paris','norway'],
    'Kishore' : ['france', 'portugal', 'new york'],
    'Sidhant' : ['london', 'bhopal', 'goa'],
}

for person,places in favorite_places.items():
    print(person.title() + "'s favorite places are :")
    for place in places:
        print("\t" + place.title())

#Favorite numbers
favorite_numbers = {
    'Jen':[2,4,6],
    'cindy':[1],
    'james':[60,59,222],
}

for person, numbers in favorite_numbers.items():
    print(person.title() + "'s favorite numbers are :")
    for number in numbers:
        print("\t" + str(number))
#cities
cities  = {
    'bangalore' : {
        'country':'india',
        'population' : 100,
        'fact' : 'This is a really green city',
    },
    'london' : {
        'country': 'united kingdom',
        'population':'10',
        'fact' : 'This is one of the most beautiful cities in the world',
    },
    'new york' : {
        'country' : 'united states',
        'population':'200',
        'fact' : 'New york is one of the best cities to stay in America'
    },
}

for city, city_info in cities.items():
    print(city)
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(country,"\t",population,"\t",fact)
#extensions

