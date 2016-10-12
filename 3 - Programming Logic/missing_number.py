def find_missing(a, b):
	#find the symmetric difference (items that are in one or the other but not both)
	missing_list = list(set(a) ^ set(b))
	return missing_list[0] if missing_list != [] else 0

print find_missing([], [])
print find_missing([4], [4])
print find_missing([1, 2], [1, 2, 5])
print find_missing([4, 6, 8], [4, 6, 8, 10])
print find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])