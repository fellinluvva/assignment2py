A = float(input("Enter real number: "))
N = int(input("Enter positive integer: "))
if N > 0:
    powers = []
    for n in range(1, N+1):
        res = A ** n
        powers.append(res)
        print(f"{A}^{n} = {res}")
    print(f"All integer powers are: {powers}")
else:
    print("Enter a positive integer")