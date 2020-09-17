#Dushyant Tara(19-06-2020): This program tells you about the modulo operation and how to use it
#The modulo operator returns the remainder
print(4 % 3)
print(5 % 3)
print(6 % 3)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
    