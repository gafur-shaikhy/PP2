# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
word = str(input('write string: '))
low = 0
Up = 0
for i in word:
    if i.islower():
        low = low + 1
    if i.isupper():
        Up = Up + 1

print(f'lower : {low} \nupper: {Up}')