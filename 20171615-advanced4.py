def combination(n,r):
    if 0 <= r <= n:
        if n == r or r == 0:
            return 1
        return combination(n-1,r-1) + combination(n-1,r)
    else:
        return "Error"

while True:
    n = int(input("Enter n:"))
    if n < 0 :
        print("Error")
        break
    r = int(input("Enter r:"))
    if r < 0 :
        print("Error")
        break
    print("C(",n,",",r,")=",combination(n,r))

