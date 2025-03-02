# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

def check_path(path):
    if os.path.exists(path):
        print("Path exist")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("File name/directory: ", filename)
        print("Path to directory: ", directory)

    else:
        print("Path doesn't exist")

user_path = input("Print path: ")
check_path(user_path)
# /Users/Lenovo/Desktop/PP2/laboratories/lab_06/exercises/files and dictionary/3.py