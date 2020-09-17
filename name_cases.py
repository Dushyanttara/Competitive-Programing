#Dushyant Tara(17-06-2020): This program tells you about importance of functions like strip, upper and lower
#person name case
person_name = "Eric topol"

message = "Hello " + person_name.title() + ", would you like to learn python today?"
print(message)


#famous author quote

author_name = "alberT EinsteiN"

famous_quote = '"A person who never made a mistake never tried anything new."'

message = author_name.title() + " once said, " + famous_quote

print(message)

#stripping names

person_name = "\t\n\teric\n\ttopol"

print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())