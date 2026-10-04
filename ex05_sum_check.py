print("Enter the first num")
a = int(input())
print("Enter the second num")
b = int(input())
print("Enter the third num")
c = int(input())

if a == b + c:
    print("the num equal to the sum of the others is:", a)
elif b == a + c:
    print("the num equal to the sum of the others is:", b)
elif c == a + b:
    print("the num equal to the sum of the others is:", c)
else:
    print("no number is equal to the sum of the other two")
