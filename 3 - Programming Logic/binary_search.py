class BinarySearch(list):

	def __init__(self, a , b):
		for x in range(1, a+1):
			list.append(self, (x*b))
		self.length = a


	def search(self,param):
	    lower = 0
	    upper = self.length-1
	    found = False
	    count = 0
	    in_list = False
	    try:
	      index = self.index(param)
	      in_list = True
	    except ValueError:
	      index = -1
	      in_list = False

	    while lower<=upper and not found and in_list and param != self[upper]:
	        middle = (lower+upper)//2
	        mid_value = self[middle]
	        if mid_value == param:
	            found = True
	            count +=1
	            index = middle
	        else:
	            if param < mid_value:
	                upper = middle - 1
	                count +=1
	            else:
	                lower = middle + 1
	                count +=1
	    return {"count": count, "index": index}


#normal testing
print BinarySearch(20,1)
bs = BinarySearch(20,1)
print bs.search(16)