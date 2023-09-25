a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

def fix_teen(n):
    return 0 if 13 <= n <= 19 else n

a = fix_teen(a)
b = fix_teen(b)
c = fix_teen(c)

print("Sum =", a + b + c)
