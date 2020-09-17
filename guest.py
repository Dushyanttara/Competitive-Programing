#Dushyant Tara(22-06-2020): This program helps us understand read, write methods in the file.

prompt = "What's your name?\n"

active = True
count = 1
while active:
    print("Enter 'q' anytime to close the program ")
    username = input(prompt)
    if username == 'q':
        active = False
        break
    print("Hi " + username.title() + ", welcome to our website!")
    filename = 'D:\Prep\python crash course book\Basics\data_files\guests.txt'
    if count == 1:
        with open(filename, 'w') as file_object:
            file_object.write(username.title() + '\n')
    else:
        with open(filename, 'a') as file_object:
            file_object.write(username.title() + '\n')
    count = 2


prompt = "Why do yo like programing?"
filename = 'D:\Prep\python crash course book\Basics\data_files\prog_poll.txt'

while not active:
    print("Enter 'q' anytime to quit the program.")
    response = input(prompt)

    if response == 'q':
        active = True
        break
    
    if count == 2:
        with open(filename, 'w') as file_object:
            file_object.write(response + '\n')
    if count == 1:
        with open(filename,'a') as file_object:
            file_object.write(response + '\n')
    
    count = 1

