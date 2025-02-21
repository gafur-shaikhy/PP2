# Write a python program to convert snake case string to camel case string.

import re

string = str(input('please write: '))

after_change = ''

for i in string:
    if i != '_':
        after_change = after_change + i


print(f'result: {after_change}')