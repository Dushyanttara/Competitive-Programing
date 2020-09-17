#Dushyant Tara(22-06-2020):This program helps you understand how to load json files and read them

import json

filename = 'D:\Prep\python crash course book\Basics\data_files\\numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)