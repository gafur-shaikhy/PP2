import re

Word = str(input('print: '))

x = re.search(r'^[A-Z]''[a-z]+$', Word)

if x :
    print('Correct')
else:
    print('Nooo')    