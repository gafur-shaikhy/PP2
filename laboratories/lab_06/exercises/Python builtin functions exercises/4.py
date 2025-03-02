# Write a Python program that invoke square root function after specific milliseconds.
import time
import math
print('Sample Input:')
san = int(input().strip())
second = float(input().strip())
time.sleep(second/1000)
print(f"Square root of {san} after {second} miliseconds is {math.sqrt(san)}")
