#Dushyant Tara(17-06-2020): This program helps understand list comprehensions and range function for ints

#Counting to twenty
for i in range(1,21):
    print(i)


#One million
one_million_list = list(range(1,10001))

for item in one_million_list:
    print(item)


#summing a million
print(min(one_million_list))
print(max(one_million_list))
print(sum(one_million_list))


#odd Numbers
odd_ns = list(range(1,20,2))

for odd_n in odd_ns:
    print(odd_n)


#threes
threes = []

for value in range(1,11):
    threes.append(value * 3)
    print(value * 3)


#cubes
cubes  = []

for value in range(1,11):
    cubes.append(value ** 3)
    print(value**3)


#cube comprehension

cubes = [x ** 3 for x in range(1,11)]
print(cubes)

