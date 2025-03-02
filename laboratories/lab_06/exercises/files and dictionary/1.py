# Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path = input("Enter the directory path: ")
if os.path.exists(path):
    items = os.listdir(path)
    print("Directories:")
    for item in items:
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    print("\nFiles:")
    for item in items:
        if os.path.isfile(os.path.join(path, item)):
            print(item)
    print("\nAll items:")
    for item in items:
        print(item)
else:
    print("The specified path does not exist!")