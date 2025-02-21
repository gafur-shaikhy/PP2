# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
# exist: "abb", "abbb", but no "a", "ab", "abbbb", "abc"
import re

abbb = str(input("print: "))

x = re.search('^abb?b$',abbb)

if x :
    print("yeah")
else:
    print("noo")    


#------------ 2nd way ---------------------#

import re

abbb = str(input("print: "))

x = re.search('ab{2,3}$',abbb)

if x :
    print("yeah")
else:
    print("noo")    