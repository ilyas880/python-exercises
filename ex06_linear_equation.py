# Solve the linear equation: ax + b = 0
print("Enter a")
a = int(input())
print("Enter b")
b = int(input())

if a == 0 and b == 0:
    print("The equation has an infinite number of solutions.")
elif a == 0:
    print("No solution (impossible equation).")
else:
    x = -b / a
    print("The solution is x =", x)
