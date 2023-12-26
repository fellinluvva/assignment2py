N = int(input("Enter a positive integer: "))

if N > 0:
    summ = 0
    res = 1
    for i in range(1, N + 1):
        res *= i
        summ += res
    print(f"The sum of factorials from 1! to {N}! is: {summ}")
else:
    print("Please enter a positive integer")
