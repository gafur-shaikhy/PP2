# Write a Python program to copy the contents of a file to another file
import os
name = str(input('print name of file.txt: '))
path = '/Users/Lenovo/Desktop/PP2/laboratories/lab_06/exercises/files and dictionary/'
new_file_path =f'{path}{name}.txt'
new_file = open(new_file_path, 'a')

file_origin = open('/Users/Lenovo/Desktop/PP2/laboratories/lab_06/exercises/files and dictionary/7.py', 'r')
text = file_origin.readlines()

for line in text:
    new_file.write(line)