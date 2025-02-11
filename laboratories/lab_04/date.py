print("  -------------- 1 ---------------------" , "\n")
import datetime
x1 = datetime.datetime.now()
previous_date = x1 - datetime.timedelta(days = 5) #крч timedelta знаечениеге даталық сан алады
print(previous_date.strftime("%d %B %Y"))

print("\n"," ---------------- 2 ---------------------", "\n")
import datetime
x2 = datetime.datetime.now()
yesterday = x2 - datetime.timedelta(days = 1) 
today = x2
tomorow = x2 + datetime.timedelta(days = 1)
print("yesterday was:",yesterday.strftime("%d %B %Y"))
print("today is:",today.strftime("%d %B %Y"))
print("tomoorow will:",tomorow.strftime("%d %B %Y"))

print("\n", "---------------- 3 ---------------------" , "\n")
import datetime
x3 = datetime.datetime.now()
print(x3.strftime("%f"))

print("\n", "---------------- 4 ---------------------", "\n")
import datetime
import math
date1 = int(input())
date2 = int(input())
print(abs(date1 - date2)*60*60*24)