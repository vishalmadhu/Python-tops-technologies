str=input("Enter Sting: ")
uc=0
lc=0
new_string=""
for i in str:
    if i.isupper():
        new_string += i.lower()
        uc=uc+1
    elif i.islower():
        lc=lc+1
        new_string += i.upper()
    
print("Total String :",str)
print("Total lower case letters :",lc)
print("Total upper case letters :",uc)
