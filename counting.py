#Dushyant Tara(19-06-2020): This program helps you understand while loop and continue
"""
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
"""
#Use continue in a while loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

#Exercises
#pizza toppings

"""active = True
prompt = "Write the topping you want to have:"
prompt += "\nEnter 'quit' to exit"
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print("We'll add " + topping + " to your pizza.")"""

#Movie tickets

"""active = True
prompt = "What is your age?"

while active:
    age = input(prompt)
    if int(age) < 3:
        price = 0
    elif int(age) < 12:
        price = 10
    else: 
        price = 15
    print("your movie ticket cost is $" + str(price) + ".")
    active = False
"""

        