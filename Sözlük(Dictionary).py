###########################################
#Sözlük(Dictionary)
###########################################


# Değiştirilebilir
# Sırasızdır(3.7 sürümünden sonra sıralı)
# Kapsayıcıdır


#key-value

dictionary = {"REG":"Regression",
            "LOG":"Logistic Regression",
            "CART": "Classification and reg"}

print(dictionary["CART"]) 

dictionary2 = {"REG":["RMSE",10],
            "LOG":["MSE",20],
            "CART": ["SSE",30]}

print(dictionary2["LOG"])

###############
#KEY SORGULAMA
print("REG" in dictionary)
###############


#################
#Value Değiştirme
dictionary["REG"]=["demo",15]
#################

#################
#tüm Key'lere ve Value'lara erişmek
dictionary.keys()
dictionary.values()
#################


#################
#Tüm çiftlere Tuple Halinde Listeye Çevirme
dictionary.items()
#################


#################
#Yeni key-value eklemek
dictionary.update({"CA":100})
################# 