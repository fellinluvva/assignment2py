a, b, c = map(int, input('Enter three whole numbers: ').split())
count_pos = 0
count_neg = 0
if a > 0:
    count_pos += 1
elif a < 0:
    count_neg += 1

if b > 0:
    count_pos += 1
elif b < 0:
    count_neg += 1

if c > 0:
    count_pos += 1
elif c < 0:
    count_neg += 1

print(f"Number of positive numbers is {count_pos}, Number of negative numbers {count_neg}")
