a = int(input("enter the number "))
b = int(input("enter the number "))
c = int(input("enter the number "))

if a>b:
    if a>c:
     print("a is bigger then b and c")
elif b>c:
    print("b is bigger then c")
elif b<a:
    print("b bigger then a")
else:
    print("c bigger then a and b")