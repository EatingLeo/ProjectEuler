for x in range(2,600851475143):
	if x % x == 0:
		print ("This is not a prime number")
	else: 
		print ("This is a prime number")

print ("This is the largest prime number" + str(max(x)))

# why the code can't print out the result?
# A: because the number you are trying to output is too big. You have to wait for a long time before you can output it 
# A: delete print("This is/isn't a prime number") may help, but the number in the range is really big anyway
# Also: if you want to use return, you have to use def, otherwise where do numbers return to?
