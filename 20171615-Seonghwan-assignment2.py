n = int(input("Enter a number:"))
while n >= 0:
    fac = 1
    for i in range(1,n+1):
        fac = fac*i
    print(n,"!=",fac)
    n = int(input("Enter a number:"))

    if n == -1:
        break
    elif n <= -2:
        print("Error!!")
        n = int(input("Enter a number:"))
