#Dushyant Tara(19-06-2020): This program helps you understand the input() function to take input from users
#Dushyant Tara(19-06-2020): This program also helps understand use of while loop and flags(global)
prompt = "\nTell me something, and I will repeat it back to you:"
prompt =  "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


"""message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
"""

#Using a flag

