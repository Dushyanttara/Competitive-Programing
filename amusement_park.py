#Dushyant Tara(18-06-2020): This program tells you about the if-elif-else chain

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
"""elif age >= 65:
    price = 5"""

print("Your admission cost is $" + str(price) + ".")

