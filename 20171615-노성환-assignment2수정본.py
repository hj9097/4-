num = 0
while num != -1:
    num = int(input("Enter a number:"))
    if num <= -2:
        print("Error")

    elif num >= 0:
        fac = 1
        for i in range(1,num+1):
            fac = fac * i
        print(num,"!=",fac)
