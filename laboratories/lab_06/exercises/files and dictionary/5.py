# Write a Python program to write a list to a file.

new_file = open("/Users/Lenovo/Desktop/PP2/laboratories/lab_06/exercises/files and dictionary/5(1).txt", 'a')

print_list = list(input("print list: \n").split())

new_file.write(str(print_list))

