#Dushyant Tara(21-06-2020): This program helps us understand how to work with open() and 'with' commands.
#Working with absolute and relative paths
#Reading line by line

file_path = 'D:\Prep\python crash course book\Basics\data_files\learning_python.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip().replace('Python','Scala'))

#Making a list of lines from a file
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip().replace('Python','C'))