def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    elif n == 0:
        return 1
    else:
        return "Error"
def combination(n,r):
    if 0 <= r <= n:
        return factorial(n) // (factorial(r) * factorial(n-r))
    else:
        return "Error"
while True:
    n = int(input("Enter n:"))
    if n == -1:
        break
    r = int(input("Enter r:"))
    if r == -1:
        break
    print("C(",n,",",r,")=",combination(n,r))
