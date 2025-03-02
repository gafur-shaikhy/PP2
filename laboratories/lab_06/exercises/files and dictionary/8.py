# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

name = str(input('print name: '))
path = '/Users/Lenovo/Desktop/PP2/laboratories/lab_06/exercises/files and dictionary/'
path_new = f'{path}{name}.txt'
new_file = open(path_new, 'a')
new_file.close()

comand = str(input(f'Do you want to remove file {name}.txt |yes or no|:  '))

if comand == 'yes':
    if os.path.exists(path_new):
        os.remove(path_new)
        print(f'delete file: {name}.txt')
        
    else:
        print("file doesn't exist")    
else:
    print('stop removing')        

#-----------------------------------------------------------------------#

# import os

# name = input('Print name: ')

# path = '/Users/Lenovo/Desktop/PP2/laboratories/lab_06/exercises/files and dictionary/'
# file_path = f'{path}{name}.txt'

# with open(file_path, 'a', encoding='utf-8') as new_file:
#     pass  # Здесь можно что-то записать в файл, если нужно

# command = input(f'Do you want to remove file {name}.txt (yes or no)? ')

# if command.lower() == 'yes':  
#     if os.path.exists(file_path):
#         os.remove(file_path)
#         print(f'Deleted file: {name}.txt')
#     else:
#         print("File doesn't exist")
# else:
#     print('Stop removing')
