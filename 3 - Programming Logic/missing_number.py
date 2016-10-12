def find_missing(a, b):
	#find the symmetric difference (items that are in one or the other but not both)
	missing_list = list(set(a) ^ set(b))
	return missing_list[0] if missing_list != [] else 0