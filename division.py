#Dushyant Tara(22-06-2020): This program helps you understand try except blocks
#Handiling the zero dvivision error exception
#using try-except blocks

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#Using Exceptions to prevent crashes
print("Give me two numbers, and I'll divide them")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0")
    else:
        print(answer)

    