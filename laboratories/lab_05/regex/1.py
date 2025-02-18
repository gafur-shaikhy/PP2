# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re
leters = str(input("print a*b: "))

x = re.search('^ab*$', leters)

if x :
    print("Yeaahhhh")
else :
    print("It is sooo wrong")    