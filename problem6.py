# square of the sum of the first ten natural numbers
total1 = (sum(range(1,101)))**2

#  sum of the squares
total2 = 1
for i in range(1,101):
	total2 += i**2
print total2

# difference
diff = total1 - total2
