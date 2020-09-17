#Dushyant Tara(17-06-2020):This program helps organize a list

#sorting a list permanently with sort()

cars = ['bmw','audi','toyota','subaru']


for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title()) 

#cars.sort()
#cars.sort(reverse = True)
print("\nHere is the sorted list:")
print(sorted(cars))#sorted is used for temporarily displaying a sorted list
print("\nHere is the original list again:")
print(cars)

#print a list in reverse order

cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars) 

#Finding the length of a list

cars = ['bmw', 'audi','toyota','subaru']

print(len(cars))


def car_store(manufacturer,model,**carinfo):
    """Store car information in a dictionary

    Args:
        manufacturer (str): Name of the manufacturer
        model (str): Model of the car

    Returns:
        Dict: A Dictionary containing all the car information
    """    
    car_dict = {}
    car_dict['manufacturer'] = manufacturer
    car_dict['model'] = model
    for key,value in carinfo.items():
        car_dict[key] = value
    return car_dict


c1 = car_store('subaru','maybach',year_purchased = 2012, distance = '70km')

print(c1)