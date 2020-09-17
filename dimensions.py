#Dushyant Tara(18-06-2020): This program helps in understading Tuples

dimensions = (200,50)
#print(dimensions[0])
#print(dimensions[1])

"""
You can't change the dimensions of a tuple
dimensions[0] = 250
"""
#Looping through all values in a tuple
print("Original dimensions:")

for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)