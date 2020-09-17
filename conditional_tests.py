#Dushyant Tara(18-06-2020): This program helps you understand conditionals by practice
#Exercises
#Conditional tests
car =  'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')


fruit = 'pineapple'
print("is fruit == 'pineapple'? I predict True")
print(fruit == 'pineapple')

fruits = ['apple','orange','mango','banana','apricot','avocado']

print("is pineapple present in your list?")
print('pineapple' in fruits)

print("is orange in the list?")
print('orange' in fruits)


cities_lived = ['Ambala', 'Chandigarh', 'Goa', 'Gurgaon', 'Bangalore', 'Mumbai','Jaipur']

print("Have you lived in Amritsar?")
print('Amritsar' in cities_lived)

print("Have you lived in Goa?")
print('Goa' in cities_lived)

friends = ['Sidhant', 'Umesh', 'Ishmin', 'Nidhi', 'Vyom', 'Clyde']

print("is Umesh your first friend?")
print(friends[0].lower() == 'Umesh'.lower())

print("is Umesh your second friend?")
print(friends[1].lower() == 'Umesh'.lower())


print("is Sidhant your close friend?")
print('Sidhant' in friends)

print("is Salim your friend?")
print('Salim' in friends)

defaulter_students = ['amar', 'modi', 'sonia', 'kejriwal','rahul' ]

student = 'arvind'
print("is Arvind a good student?")
print(student not in defaulter_students)
print("\nsite loads")
page1_loads = 100
page2_loads = 200
page3_loads = 500
page4_loads = 600

print((page1_loads >= 100) and (page2_loads < 1000))
print((page1_loads > 50) or (page3_loads > 5000))
print((page3_loads < 5000) and (page4_loads > 50))

