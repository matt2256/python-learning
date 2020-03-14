def unique_list(lst):
	x = []
	for s in lst:
		if s not in x:
			x.append(s)
	return x


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
