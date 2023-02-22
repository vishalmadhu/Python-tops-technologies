a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b or b == c or c == a:
    print("Sum is zero, as two or three number are equal.")
else:
    print("Sum of the number is:", a + b + c)
