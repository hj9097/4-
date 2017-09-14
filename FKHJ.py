result = 1
num = int(input("enter a number: "))

while (num != -1):
	if num < -1:
		print("error")
		num = int(input("enter a number: "))

	for i in range(num):
		result = result * (i + 1)
	print(result)
	num = int(input("enter a number: "))
	result = 1
	
	
