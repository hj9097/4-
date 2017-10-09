import time

def iterfibo(n):
    ct = 0
    a = 1
    b = 1
    c = 0
    while True:
        if ct <= n-3:
            c = a
            a = a + b
            b = c
            ct += 1
        elif n == 0:
            return 0
        else:
            return a

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
