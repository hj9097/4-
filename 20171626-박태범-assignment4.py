def factorial(n):
    ans = 1
    if n >= 0:
        for i in range(1, n+1):
            ans = ans*i
        return ans

a = 0    #계속 루프를 돌기 위해 임의의 a 지정

while a != -1:
    n = int(input("Enter n : "))
    if n == -1:    #n이 -1로 입력받으면 종료
        break
    a = factorial(n)
    m = int(input("Enter m : "))

    if n < 0 or m < 0:     #n이 -1이 아닌 음수 또는 m이 음수인 값을 입력받으면 에러메세지 출력
        print("올바른 값을 입력하세요")
        continue

    if n == 0 and m != 0:  #n이 0이고 m은 0이 아닐때 에러메세지 출력
        print("Error")
        continue

    b = factorial(m)
    c = factorial(n-m)


    com = int(a/(b*c))
    print("C(",n,",",m,") = ",com)
