n=input()
c=0 
for i in n:
    
    if ord(i)>122:
        c+=1 
    elif ord(i)<97 and ord(i)>90:
        c+=1 

    elif  ord(i)<65:
        c+=1 
print(c) 
