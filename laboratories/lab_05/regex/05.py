# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

ab = str(input('print: '))

x = re.search(r'^a.*b$', ab)

if x :
    print('good')
else:
    print('no')    