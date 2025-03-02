# Write a Python program to count the number of lines in a text file.
import os
def cou_line(path_f):
    if os.path.exists(path_f):
        with open(path_f, 'r') as f:
            lines = f.readlines()
            return(print(f'number of lines: {len(lines)}'))

    else :
            print("Path doesn't exist.")

path_of_file = input("print path: ")
cou_line(path_of_file)             