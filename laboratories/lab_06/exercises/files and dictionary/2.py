# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os
path = str(input("Enter the directory path: ")) #print /Users/Lenovo/Desktop/PP2/laboratories/lab_06/exercises 
print(os.access(path, os.F_OK)) # Existence
print(os.access(path, os.R_OK)) # Readability
print(os.access(path, os.W_OK)) # Writeability
print(os.access(path, os.X_OK)) # Executeability