x = int(input('Enter a whole number: '))
if x > 0:
    res = x + 1
elif x < 0:
    res = x - 2
else:
    res = 10
print(f"Result number: {res}")