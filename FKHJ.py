a = 1
x = int(input("enter a number: "))

while (x != -1):
	for i in range(x):
		a = a * (i + 1)
	print(a)
	x = int(input("enter a number: "))
	a = 1
						
