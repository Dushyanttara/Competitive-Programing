#Dushyant Tara(17-06-2020): This program helps understand all the functions we use in lists organization

"""cities = ['goa', 'delhi', 'ambala', 'chandigarh', 'bangalore', 'mumbai', 'jaipur']

cities.append('surat')

remove_city = 'mumbai'

cities.remove('mumbai')

print(cities)
print(remove_city)
rem_city = cities.pop(0)

print(rem_city, " is one of the most beautiful places i've been to") 

del cities[4]
print(cities)
print(sorted(cities))

print(sorted(cities, reverse = True))

cities.reverse()

print(cities) """
#Dushyant Tara(19-06-2020): This program helps you understand the use of break in a while loop
#Using break in a loop
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

