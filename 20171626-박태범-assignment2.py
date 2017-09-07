a = int(input("enter a number: "))
ans = 1

if a >= 0:
    while a>=0:
        for i in range(a):
            b=i+1
            ans=ans*b
        print(a,"! =",ans)
        ans = 1
        a = int(input('enter a number: '))
else:
    print('end')
