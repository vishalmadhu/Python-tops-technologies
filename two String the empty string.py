str=input("Enter String: ")

if len(str)< 2:
    result= ""
else:
    result= str[:2]+ str[-2:]
print(result)
