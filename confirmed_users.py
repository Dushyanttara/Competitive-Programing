#Dushyant Tara(19-06-2020): This program helps you understand the working of while loop
#with lists and dictionaries

#Start with users that need to be verified
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#verify each user until there are no more unconfirmed users.
#Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
#Displaying all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


