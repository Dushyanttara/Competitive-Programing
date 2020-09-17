#Dushyant Tara(17-06-2020): This program helps you understand list operations

#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles[0] = 'ducati'

#motorcycles.append('ducati')

#motorcycles = []

#motorcycles.append('honda')
#motorcycles.append('yamaha')
#motorcycles.append('suzuki')
#usually insert will shift every other element from the position to the right
#motorcycles.insert(0,'ducati')

#Removing elements from a list
#print(motorcycles)

#del motorcycles[1]
#print(motorcycles)

#pop from a list
#motorcycles = ['honda', 'yamaha', 'suzuku']
#print(motorcycles)

#last_owned = motorcycles.pop()
#print("The last motorcycle I owned was a " + last_owned.title() + ".")

#pop from anywhere in the list
#motorcycles = ['honda','yamaha', 'suzuki']

#first_owned = motorcycles.pop(0)
#print('The First motorcycle I owned was a ' + first_owned.title() + '.')

#Remove an item by value, remove method only removes the first occurence of the element
#for recursively removing use loops

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

