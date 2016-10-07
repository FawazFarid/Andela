# def prime(num):
# 	for n in range(0, num+1):
# 	    if all(n%i!=0 for i in range(2,n)):
# 	    	print n
# prime(10)
# 

def prime(num):
	for n in range(2, num+1):
		prime = True
		for i in range(2, n):
			if n%i==0:
				prime=False
		if prime:
			print n;

prime(10)