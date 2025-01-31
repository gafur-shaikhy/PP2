# class Student :
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a
#         print(n)

# Student("Gafur", 17).__init__
#it is simmilar 

# class Student:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a
#         print(n)

# st = Student("Gafur", 17)

class Student :
    def __init__(self, n, a):
        self.name = n
        self.age = a
        print(n)

Student("Gafur", 17)


class The_best:
    def __init__(self, j, h):
        self.jersey = j
        self.number = h
    
    def __str__(self):
        return f"{self.jersey} {self.number}"

print(The_best("Cristiano Ronaldo", 7))