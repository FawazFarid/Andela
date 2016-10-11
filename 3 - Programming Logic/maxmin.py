def find_max_min(num_list):
	num_list.sort()
	return [num_list[0], num_list[-1]] if (num_list[0] != num_list[-1]) else [num_list[0]]