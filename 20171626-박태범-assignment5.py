import time
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)
def fibo2(n):
    if n <= 1:
        return n
    else:
        tmp = 1
        ans = 1
        last = 0
        for i in range (1,n):
            tmp = ans
            ans += last
            last = tmp
        return ans



while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber,ts))
    ts2 = time.time()
    fibonu = fibo2(nbr)
    ts2 = time.time() - ts2
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonu, ts2))
