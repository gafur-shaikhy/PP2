# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re 

lower_case = str(input("print word: "))

x = re.search(r'_', lower_case)

if x :
    print('It is correct')
else:
    print('WRITE WITH UNDERSCORE!!!!!!!')    