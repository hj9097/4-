def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    elif n == 0:
        return 1
    else:
        return "Error"
n = 0
while n != -1:
    n = int(input("Enter a number:"))
    print(factorial(n))
