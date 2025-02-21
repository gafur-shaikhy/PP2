# Write a Python program to insert spaces between words starting with capital letters.


import re
def insert_spaces(text):
    result = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return result
input_text = str(input())
output_text = insert_spaces(input_text)
print("Original:", input_text)
print("Modified:", output_text)