def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

num = int(input("Enter a positive number: "))
print("Sum from 1 to", num, "=", sum_numbers(num))
