#Dushyant Tara(22-06-2020): This program helps you understand typeerror and how to handle it



while True:
    print("Enter two numbers, and I will provide you their addition")
    print("Enter 'q' anytime to quit the program.")
    number1 = input("Enter the first number: ")
    if number1 == 'q':
        break
    number2 = input("Enter the second number: ")
    if number2 == 'q':
        break
    try:
        addition = int(number1) + int(number2)
    except ValueError:
        msg = "please input integers and not text"
        print(msg)
    else:
        print(addition)