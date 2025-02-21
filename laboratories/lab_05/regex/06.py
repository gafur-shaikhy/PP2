# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

string = str(input('print: '))
after_change = ''

for i in string:
    if i == ' ' or i == ',' or i == '.' :
        i = ':'
        after_change = after_change + i
    else:
        after_change = after_change + i

        
print(f'after_change: {after_change}')        