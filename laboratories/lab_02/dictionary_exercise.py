very_big_dict = {
 "sub_dict1" : {
     "street" : "TB",
     "floor" : 4   
 },

 "sub_dict2" : {
     "street" : "Ab",
     "floor" : 1
 }
}

for subdict, key_val in very_big_dict.items(): #для подмножество, каждый ключ-значение внутри большого подмножество
    print(subdict)

    for key in key_val:
        print(key,":", key_val[key])    
