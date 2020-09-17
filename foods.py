#Dushyant Tara(17-06-2020): This program will help you understand copying a list

my_foods = ['pizza', 'falafel', 'carrot cake','gulab jamun','cutlet','momos','aloo paratha']
friend_foods = my_foods[:] #Remember to copy the list using a slice
my_foods.append('ice cream')

friend_foods.append('cannoli')

print("My favorite foods are : ")
for my_food in my_foods:
    print(my_food)

print("\n My friend's favorite foods are: ")

for friend_food in friend_foods:
    print(friend_food)


print("The first three items in the list are : ")
print(my_foods[:3])
print("The three items fromt the middle of the list are")
print(my_foods[int(len(my_foods)/2): ])

print("The last 3 items in the list are")
print(my_foods[-3:])