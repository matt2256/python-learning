def multiply(num):
	count = 1
	for s in num:
		count *= s
	return count


print(multiply([1, 2, 3, -4]))
