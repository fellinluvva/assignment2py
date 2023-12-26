print("Enter A < B")
A = int(input("Enter the first integer: "))
B = int(input("Enter the second integer: "))
if A < B:
    n = B - A + 1
    result = (n * (A + B)) // 2
    print(f"The sum of integers between {A} and {B} is: {result}")
else:
    print("A is less than B, make sure to enter values A < B")
