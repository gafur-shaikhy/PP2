# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
letters = []
for i in range(26):
    char = chr(65+i)
    letters.append(char)

directory = "/Users/Lenovo/Desktop/PP2/laboratories/lab_06/exercises/files and dictionary/"

for letter in letters:
    file_path = f'{directory}{letter}.txt'
    new_file = open(file_path, 'a')
    new_file.write(str({letter}))
        