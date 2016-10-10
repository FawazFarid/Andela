def fizz_buzz(num):
	#if the number is divisible by both 3 and 5
	if(num%3 ==0 and num%5==0):
		return "FizzBuzz"
	else:
		#if number is divisible by 3 only
		if(num%3 == 0):
			return "Fizz"	
		#if number is divisble by 5 only
		elif(num%5 == 0):
			return "Buzz"	
		#number not divisible by 3 or 5
		else:
			return num