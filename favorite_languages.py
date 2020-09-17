#Dushyant Tara(19-06-2020):This program helps you understand dictionaries to save same object
#for multiple people

#A dictionary of similar objects
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

print("Sarah's favorite language is: " + 
    favorite_languages['sarah'].title() + 
    ".")

for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".\n")

friends = ['phil','sarah']

#looping through all the keys in a dictionary
for name in favorite_languages.keys():#Keys are set as default so 'for namein favorite_languages' would 
                                    #would return something similar
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll\n")

#Looping through a dictionary's keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + " thank you for taking the poll")

#Looping through all the values in a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#See values without repition using a set
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
  

"""
#Exercises
##Person
Person = {'first_name': 'Dushyant','last_name':'Rai Tara', 'age':24, 'city':'Bangalore'}

for key in Person:
    print(key," ",Person[key])

#Favorite Numbers
favorite_numbers = {
    'james':5,
    'mia':11,
    'andrew':9,
    'Jhon':7,
    'Jacob':8,
}

for key,value in favorite_numbers.items():
    print(key,":", value)
"""
#Glossary
glossary = {
    'conditionals':'These are used for boolean check',
    'loops':'These are used to loop through iterators to repeat some process',
    'list':'List stores values of same or differnt type and is mutable',
    'tuple':'Tuples are very similar to lists but they are immutable',
    'dictionary':'Dictionaries are object storage structure, you can store any python object in it',
    'dictionary loops': 'Looping through keys and values in a dictionary helps in traversel',
}
print("\nI have learnt the following in previous few lessons:")
for key,value in glossary.items():
    print("\n",key,":\n",value)

#Rivers
rivers = {
    'nile' : 'egypt',
    'narmada' : 'india',
    'thames' : 'united kingdom'
}

for river,country in rivers.items():
    print("\nThe " + river.title() + " runs through " + country.title() + ".")

for river in rivers.keys():
    print(river.title())

for country in set(rivers.values()):
    print(country.title())


#Polling


new_users = ['edward','phil','vyom','abhinav','gaurav']

for user in new_users:
    if user in favorite_languages.keys():
        print(" Hi " + user.title() + " thanks for taking the poll")
        print("glad to know that your favorite langauge is " + favorite_languages[user].title() + "!")
    else:
        print(" Hi " + user.title() + " please take the poll")

#Dushyant Tara(19-06-2020):storing lists inside a dictionary

favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil' : ['python','haskell'],
}

for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite langauges are :")
    for language in languages:
        print("\t" + language.title())
    

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

        
