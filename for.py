import time

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

def iterfibo(n):
    if n <= 1:
        return n
    fibolist=[0,1]
    for i in range(2,n+1):
        fibolist.append(fibolist[i-2] + fibolist[i-1])
    return fibolist[-1]
while True:
        n = int(input("Enter a number:"))
        if n == -1:
            break
        ts = time.time()
        fibonumber = fibo(n)
        ts = time.time() - ts
        print("Fibo(%d)=%d,time%.6f" % (n,fibonumber,ts))
        ts2 = time.time()
        iterfibonumber = iterfibo(n)
        ts2 = time.time() - ts2
        print("Iterfibo(%d)=%d,time%.6f" % (n,iterfibonumber,ts2))
