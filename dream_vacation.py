#Dushyant Tara(19-06-2020): This program helps create a poll using while loop and dictionaries

#create an empty list for the poll responses
responses = {}

#create a flag of poll active and set it to true
poll_active = True

while poll_active:
    name = input("What is your name?")
    response = input("If you could visit one place in the world where would you go?")

    responses[name.title()] = response

    retake_ = input("Would you like someone else to fill the poll after you? (yes/no)")
    if retake_.lower() == 'no':
        poll_active = False

#Poll results
print("\n---Poll Results---")
for name, response in responses.items():
    print(name + " wants to go to " + response + ".")
