def factorial(n):
	ans = 1
	if n >= 0:
		for i in range(1, n+1):
			ans = ans*i
		return ans
	else:
		print("Error")

n = int(input("Enter n : "))
a = factorial(n)
m = int(input("Enter m : "))
b = factorial(m)
c = factorial(n-m)

com = a/(b*c)
print(com)
