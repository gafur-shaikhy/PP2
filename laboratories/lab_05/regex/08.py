# Write a Python program to split a string at uppercase letters.
import re
def split_at_uppercase(s):

    parts = re.split(r'(?=[A-Z])', s)
    parts = [part for part in parts if part]

    return parts


input_string =str(input())
result = split_at_uppercase(input_string)

print("Original string:", input_string)
print("Split parts:", result)