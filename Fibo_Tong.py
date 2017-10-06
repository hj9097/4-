import time

def fibo_iter(n) :
    fb = [0, 1]
    if n>2 :
        for i in range (1,n) :
            for j in range (i-1,i):
                fb.append(fb[j]+fb[i])
        return fb[-1]
    else :
        return fb[n]

def combin(n,r):
    if 0 <= r <= n:
        if n == r or r == 0:
            return 1
        return combin(n-1,r-1) + combin(n-1,r)
    elif n == 0 and r > 0 :
        return 0

def fibo_cob(n) :
    answer = 0
    for i in range(1,n+1) :
        answer +=(combin(n,i))*(((5**0.5)**(i))-((-(5**0.5))**i))
    return answer//((2**n)*(5**0.5))


number = int(input("Enter number: "))
ts = time.time()
print(fibo_iter(number))
ts1 = time.time()-ts
print(int(fibo_cob(number)))
ts2 = time.time()-ts1
print(ts1, ts2)