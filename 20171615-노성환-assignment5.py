import time

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

def iterfibo(n):
    if n <= 1:
        return n
    result = 0
    fibo0 = 0
    fibo1 = 1
    for i in range(2,n+1):
        result = fibo0 + fibo1
        fibo0 = fibo1
        fibo1 = result
    return result
    

    
while True:
    n = int(input("Enter a number:"))
    if n == -1:
        break
    ts = time.time()
    fibonumber = fibo(n)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time%.6f" % (n,fibonumber,ts))
    ts2 = time.time()
    iterfibonumber = iterfibo(n)
    ts2 = time.time() -ts2
    print("Iterfibo(%d)=%d, time%.6f" % (n,iterfibonumber,ts2))
