#Dushyant Tara(22-06-2020): This program helps you understand json format

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'D:\Prep\python crash course book\Basics\data_files\\numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

