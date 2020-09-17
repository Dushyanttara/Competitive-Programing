#Dushyant Tara(17-06-2020): This program helps understand for loop application on lists

magicians = ['alice', 'david', 'carolina']

"""for magician in magicians:
    print(magician.title(), ", that was  great trick!")
    print("I can't wait to see your next trick, ", magician.title() , ".\n") 


print("Thank you, everyone. That was a great magic show!")"""

#Dushyant Tara(20-06-2020):This program helps you understand functions with lists

def make_great(magicians_list):
    for magician in magicians_list:
        magician = 'Great' + magician 
    print(magicians_list)

def show_magicians(magicians_list):
    for magician in magicians:
        print(magician.title())


magicians = ['alice', 'david', 'carolina']

make_great(magicians)
print(magicians)
show_magicians(magicians)
