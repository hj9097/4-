
def factorial(n) :
    if (n==1) or (n==0) :
        return 1
    else :
        return factorial(n-1)*n

def nCr (n,r) :
    T = 1
    T = T*factorial(n)/(factorial(r)*factorial(n-r))
    return int(T)

def combin(n,r) :
    if n == 0 and r==0: return 1
    if r > n or r < 0 : return 0
    else :
        return combin(n-1,r-1)+combin(n-1,r)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(nCr(num1, num2))
print(combin(num1, num2))