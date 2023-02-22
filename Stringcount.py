s = input("Enter string: ")


wd=1
ch=0
sp=0 
nb=0
sc=0

for i in s:
    if i.isspace():
        sp=sp+1
        wd=wd+1
    elif i.isalpha():
        ch=ch+1
    elif i.isnumeric():
        nb=nb+1
else:
    sc=sc+1
print("total space",sp)
print("total word",wd)
print("total alpha",ch)
print("total numberic",nb)
print("total special character",sp)
