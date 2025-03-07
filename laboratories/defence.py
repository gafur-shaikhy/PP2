import re

def split_parts(ori):
    split = re.split(r'(?=[A-Z])', ori)
    split = [el for el in split if el]

    return split

origin = str(input('print: '))
fun = split_parts(origin)
print(fun)