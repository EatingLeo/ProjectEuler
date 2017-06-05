# problem10.py

total = 0
def is_prime(x):
	if x < 2:
		return False
	for n in range(2,2000000):
		if x % n == 0:
			return False
	else:
		return True
		print sum(x)
