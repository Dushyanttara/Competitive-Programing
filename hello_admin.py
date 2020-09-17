#Dushyant Tara(18-06-2020):This program helps understand conditionals along with loops and list

#Hello Admin
usernames = ['admin','ahmad','vyom','abhinav','gaurav']

#usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            greet_message = "\nHello " + username + ", would you like to see a status report?"
        else:
            greet_message = "\nHello " + username + ", thank you for logging in again"
        print(greet_message)
else:
    print("We need to find some users")

current_users = ['Abhinav','Vyom','Arun','Gaurav','Swamil','Tanusha']

new_users = ['AbhinAv','SwamIl','NishanT','abhishek','Ritwik']

for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print("Username " +new_user + " is already in use, you need to use a new name")
    else:
        print(new_user + " is available.")


#Ordinal Numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number_ in numbers_list:
    if number_ == 1:
        ord_rep = str(number_) + "st"
    elif number_ == 2:
        ord_rep = str(number_) + "nd"
    elif number_ == 3:
        ord_rep = str(number_) + "rd"
    else:
        ord_rep = str(number_) + "th"
    print("\n" + ord_rep)