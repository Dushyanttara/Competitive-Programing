cat_filename = 'D:\Prep\python crash course book\Basics\data_files\cats.txt'
dog_filename = 'D:\Prep\python crash course book\Basics\data_files\dogs.txt'

filenames = [cat_filename,dog_filename]

for filename in filenames:
    
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Can't find " + filename + " at given location"
        #print(msg)
        pass
    else:        
        print(contents)

filename = 'D:\Prep\python crash course book\Basics\data_files\learning_python.txt'
with open(filename) as f_obj:
    counter = 0
    contents = f_obj.read()
    counter += contents.lower().count('python')
    
print(counter)
