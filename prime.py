def prime(num):
	for n in range(0, num+1):
	    if all(n%i!=0 for i in range(2,n)):
	    	print n