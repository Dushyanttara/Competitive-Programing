#Dushyant Tara(17-06-2020): This program helps understand list operations using a guest list

guest_list = ['Ishmin singh','Umesh pathak', 'Sidhant gupta']

invite1 = "Hi " + guest_list[0].title() + " would you like to come to party?"
invite2 = "Hi " + guest_list[1].title() + " would you like to come to party?"
invite3 = "Hi " + guest_list[2].title() + " would you like to come to party?"

print("\t",invite1,"\n", "\t",invite2, "\n","\t", invite3)

no_rsvp = 'Ishmin singh'

new_person = 'Shantanu sharma'
print("\n\nunfortunately ", no_rsvp, " won't be able to make it to our party\n\n")
guest_list.remove(no_rsvp)
guest_list.insert(0,new_person)

invite1 = "Hi " + guest_list[0].title() + " would you like to come to party?"
invite2 = "Hi " + guest_list[1].title() + " would you like to come to party?"
invite3 = "Hi " + guest_list[2].title() + " would you like to come to party?"

print("\t",invite1,"\n", "\t",invite2, "\n","\t", invite3)

#More Guests
print("\n\nHi Everyone, I have found a bigger dinner Table!\n\n")

new_person1 = 'Clyde bailey'
new_person2 = 'Saket soneji'
new_person3 = 'Samyak tatia'
guest_list.insert(0,new_person1)
guest_list.insert(3,new_person2)
guest_list.append(new_person3)

invite1 = "Hi " + guest_list[0].title() + " would you like to come to party?"
invite2 = "Hi " + guest_list[1].title() + " would you like to come to party?"
invite3 = "Hi " + guest_list[2].title() + " would you like to come to party?"
invite4 = "Hi " + guest_list[3].title() + " would you like to come to party?"
invite5 = "Hi " + guest_list[4].title() + " would you like to come to party?"
invite6 = "Hi " + guest_list[5].title() + " would you like to come to party?"
print("\t",invite1,"\n", "\t",invite2, "\n","\t", invite3, "\n","\t", invite4, "\n","\t", invite5, "\n","\t", invite6)

print("I am inviting " , len(guest_list), " guests to the party")

#shrinking guest list
print("\n Really Sorry everyone but we can only invite 2 people for the party")

rem_person = guest_list.pop()
print("Really Sorry " + rem_person + " you are not invited to the party anymore")

rem_person = guest_list.pop()
print("Really Sorry " + rem_person + " you are not invited to the party anymore")

rem_person = guest_list.pop()
print("Really Sorry " + rem_person + " you are not invited to the party anymore")

rem_person = guest_list.pop()
print("Really Sorry " + rem_person + " you are not invited to the party anymore")

invite1 = "Hi " + guest_list[0].title() + " would you like to come to party?"
invite2 = "Hi " + guest_list[1].title() + " would you like to come to party?"

print("\n\t", invite1,"\n\t", invite2)

del guest_list[1]
del guest_list[0]

print(guest_list)