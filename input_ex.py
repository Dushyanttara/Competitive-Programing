#Dushyant Tara(19-06-2020):This program helps you understand input function through exercises
#Rental Car
car = input("What kind of a rental car would you like?\n")
print("Let me see if I can find you a " + car)

#Restaurant Seating
dinner_group = int(input("How many people are there in your dinner group?\n"))

if dinner_group > 8:
    print("Really sorry, but you will have to wait for a table.")
else:
    print("your table is ready")

#Multiples of Ten
reported_number = input("Please input any number:\n")
reported_number = int(reported_number)
if reported_number % 10 == 0:
    print("It is a multiple of 10")
else:
    print("It is not a multiple of 10")