print("Enter the first number")
number1 = int(input())
print("Enter the second number")
number2 = int(input())

if (number1 > 0 and number2 > 0) or (number1 < 0 and number2 < 0):
    print("le produit est positif")
else:
    print("le produit est negatif")
