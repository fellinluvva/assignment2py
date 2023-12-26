print("N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2")
N = int(input("Enter a positive integer N: "))
if N > 0:
    summ = 0
    for n in range(N, 2 * N + 1):  # N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2
        summ += n**2
    print(f"The sum of the expression for N is {summ}")
else:
    print("Enter a positive integer")
