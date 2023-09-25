a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

if a == b or b == c or a == c:
    print("Sum is 0 because two numbers are equal.")
else:
    print("Sum:", a + b + c)
