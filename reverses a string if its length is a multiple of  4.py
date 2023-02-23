str=input("Enter String: ")

if len(str)% 4 == 0:
    str=str[::-1]

print(str)