A = int(input("Enter the first integer: "))
B = int(input("Enter the second integer: "))
if A < B:
    prod = 1
    for n in range(A, B + 1):
        prod *= n
    print(f"Product of integers from {A} to {B} is: {prod}")
else:
    print("A is less than B, make sure to enter values A < B")


'''
# practice lesson 26.12.23 checked by Mr. Akhmetov
list1 = [5, 3, 2, 14, 4]

print(list1[2:5])
print()

list1.insert(2, 5)
print(list1)
print()

list1.sort()
if 14 in list1:
    print("14 exists.")
else:
    print("14 does not exist.")
print()

print("List in reverse order:", list1[::-1])
'''
