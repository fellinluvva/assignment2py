a, b, c = map(float, input("Enter three numbers: ").split())

numbers = [a, b, c]
numbers.sort(reverse=True)
sum_two = numbers[0] + numbers[1]
print(f"The sum of two largest numbers is {sum_two}")
