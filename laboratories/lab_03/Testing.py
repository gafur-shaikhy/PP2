# def tst():
#     a = input()
#     b = input()
# tst()

lang = input()
def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "kz":
        print("Salem")   
    elif type(int(lang)) is int and int(lang) in range(1, 10):
            print("It is number")   
    else: 
         print("Hello")

greet(lang)    