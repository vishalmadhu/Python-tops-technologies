num = int(input("enter the number of rows:"))
ch = 64

#numbers continus oder patten 
sum = 0
for i in range(1,num+1):
    for j in range(1,i+1):
        sum = sum+1
        print("{0}".format(sum),end=" ")
    print()

#patten 
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#revers patten
for i in range(num, 0 ,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#traiangle patten 
for i in range(num-1, 0 ,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#row and column print
for i in range(1,num+1):
    for j in range(1,i+1):
        print("{0}{1}".format(i,j),end=" ")
    print()

#alfabetical chareter patten 
for i in range(1,num+1):
    for j in range(1,i+1):
        print("{0}".format(chr(ch+i)),end=" ")
    print()

#alfabatic charater continus patten 
for i in range(1,num+1):
    for j in range(1,i+1):
        ch=ch+1
        print("{0}".format(chr(ch)),end=" ")
    print()
    