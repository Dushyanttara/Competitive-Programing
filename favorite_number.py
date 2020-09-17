#Dushyant Tara(22-06-2020):This program helps you understand input(), json.dump() , with and open()

import json

def get_num_from_file():
    filename= "D:\Prep\python crash course book\Basics\data_files\\favorite_number.json" 
    try:
        with open(filename) as f_obj:
            fav_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_num


def get_num_from_user():
    fav_num = input("What is your fav number? ")
    filename= "D:\Prep\python crash course book\Basics\data_files\\favorite_number.json"
    with open(filename, 'w') as f_obj:
        json.dump(int(fav_num),f_obj)
    return fav_num

def fav_num():
    fav_num = get_num_from_file()
    if fav_num:
        print("your fav num is " + str(fav_num))
    else:
        fav_num = get_num_from_user()
        print("your fav num is " + str(fav_num))


fav_num()