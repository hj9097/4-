def factorial(n):
    ans = 1
    if n >= 0:
        for i in range(1, n+1):
            ans = ans*i
        return ans


while True:
    try:
        n = int(input("첫번째 숫자를 입력하세요 : "))
        if n == -1:    #n이 -1로 입력받으면 종료
            break
  
        m = int(input("두번째 숫자를 입력하세요 : "))
    except:
        print("올바를 숫자를 입력하세요")
        continue

    if n < 0 or m < 0:     #n이 -1이 아닌 음수 또는 m이 음수인 값을 입력받으면 에러메세지 출력
        print("올바른 값을 입력하세요")
        continue

    elif n == 0 and m > 0:  #n이 0이고 m이 0이면 0출력
        print("0")
        continue
    elif n == 0 and m < 0:  #n이 0이고 m이 음수면 에러메세지 출력
        print("올바를 숫자를 입력하세요")
        continue

    elif n < m:            #n이 m보다 작으면 에러메세지
        print("올바를 숫자를 입력하세요")
        continue

    a = factorial(n)
    b = factorial(m)
    c = factorial(n-m)


    com = int(a/(b*c))
    print("C(",n,",",m,") = ",com)
