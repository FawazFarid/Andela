def fibonacci(n):
	for i in range(0, n+1):
		a = 0
		b = 1
		for i in range(0, i):
			temp = a
			a = b
			b = temp + b
		print a

# Display the first 15 Fibonacci numbers.


fibonacci(14);