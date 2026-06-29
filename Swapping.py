a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("\nBefore swapping:")
print("First number = 5", a)
print("Second number = 10", b)


a, b = b, a

print("\nAfter swapping:")
print("First number = 10", a)
print("Second number = 5", b)
