# class Person:
#     def __init__(self, name = '', age = 0, year = 0):
#         self.name = name
#         self.age = age
#         self.year = year
     
# class Student(Person):

#     def get(self):
#         self.name = str(input('Name of the Student: '))
#         self.age = int(input('Age of the Student: '))
#         self.year = int(input('Course of the Student: ')) 

#     def check(self):
#         if self.year == 0 :
#             print(self.name.upper())
#         else:
#             print(self.name, self.age)    


# q = Student() 
# q.get()
# q.check()
 
class Fun:

    def __init__ (self, str):
        self.str = str

    def upp_f(self):
       self.str =  self.str[0].upper() + self.str[1 :]
       print(self.str)

    def rev_f(self):
       print(self.str[::-1])

str = input()
str = Fun(str)
str.upp_f()
str.rev_f()

# a = Fun('gafur')