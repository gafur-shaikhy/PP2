def gafur_rec(k):
    if k > 0 :
        res = k + gafur_rec(k - 2)
        print(res)

    else :
        res = 0
        print(res)

    return res    
gafur_rec(6)

def gafur_rec(name):
    print(name + ", how old are you?")
gafur_rec("Gafur")
gafur_rec("Damir")
gafur_rec("Yusuf")  

def fun(*var):
    print(var[0] + " University")
fun("Kazakh British Technical", "Narxoz", "Nazarbaiev")


def hhh(**t):
    print("Alma - " + t["correct"])
hhh(op1 = "orda", op2 = "meshit", correct = "ata")  
  


