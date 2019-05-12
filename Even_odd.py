#Program to check if a number is even or odd.

try:
	while True:
		try:
			while True:
				num = int(input("Enter a number: "))
				if num < 0 :
					print("Please enter positive integer only")
				else:
					if num % 2 == 0 :
						print("{0} number is even".format(num))
					else:
						print("{0} number is odd".format(num))
		except ValueError:
			print("That was not a valid number.")
except KeyboardInterrupt:
	print("User terminated the program")
	

 
 
 
 
 		
 

 



