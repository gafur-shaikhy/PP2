#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
word = str(input())
rev_w = word[::-1]
if word == rev_w:
    print("palindrome")
else :
    print("no palindrome")    