str = input("Enter String: ")
insert = input("Enter middle string:")

middle = len(str) // -2
result = str[:middle] + " " + insert + " " + str[middle:]+ " "

print(result)