#Dushyant Tara(19-06-2020): This program will help you understand while loop through exercises

sandwich_orders = ['aloo tikki','bbq chicken','ceasers','pastrami', 'tuna','cheese','pastrami','paneer tikka','ham','pastrami']

finished_sandwiches = []
print("The Deli has run out of Pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nThese are the final orders:")
for sw in sandwich_orders:
    print(sw)
while sandwich_orders:
    current_sw = sandwich_orders.pop()
    finished_sandwiches.append(current_sw)
    print("I made you a " + current_sw + " sandwich.")

print("\nThe following sandwiches have been made: ")
for sw in finished_sandwiches:
    print("\n"+sw)


