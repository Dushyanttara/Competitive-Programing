#Dushyant Tara(18-06-2020): This program helps you understand the differences between normal if and elif blocks

#Alien colors 1
alien_color = 'green'


if alien_color == 'green':
    print("Congratulations!! you just earned yourself 5 points")
elif alien_color == 'yellow':
    print("Congratualations! you have won 2 points")


#Alien colors 2
alien_color = 'yellow'

if alien_color == 'green':
    points = 5
else:
    points = 10

print("\nCongratulations!! you have just won " + str(points) + " points.")

alien_color = 'red'
#alien_color = 'green'
#alien_color = 'yellow'
#Alien Colors 3
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15

print("\nCongratulations!! you have won " ,points , "points.")

#Stages of life
age = 40

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
elif age >= 65:
    stage = 'elder'

print("\nyou are a", stage)


#Favorite Fruit
favorite_fruits = ['apple','orange','mango','strawberries','banana','guava','litchi']

if 'apple' in favorite_fruits:
    print("I really like apple!")
if 'banana' in favorite_fruits:
    print("I really like bananas!") 
if 'pomegranate' in favorite_fruits:
    print("I really like pomegranate")
if 'guava' in favorite_fruits:
    print("I really like guava")