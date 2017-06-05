

def fib(n):
	a,b = 1,1
	for i in range(n-1):
		a = b
		b = a + b
	return a

sum = 0
i = 0
while fib(i) < 4000000:
	if (fib(i) % 2 == 0):
		sum = sum + fib(i)
	#print fib(i)
	#list[i] = fib(i)
	i = i + 1

print("sum is: " + str(sum))