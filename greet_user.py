#Dushyant Tara(22-06-2020): This program helps you understand using json files 

import json

filename = 'D:\Prep\python crash course book\Basics\data_files\\username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")