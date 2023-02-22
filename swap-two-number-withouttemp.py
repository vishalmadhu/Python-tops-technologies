#swaping two number without using temp variable
a=int(input("Enter number A: "))
b=int(input("Enter number B: "))

c = a
a = b
b = c

print("your swaping number A is:" ,a)
print("your swaping number B is:" ,b)