import random
print("hello word")



karak= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
p_u=int(input("kaç haneli parola olsun"))
parola=""
for i in range(p_u):
    karakter=random.choice(karak)
    
    parola+=karakter
print(parola)