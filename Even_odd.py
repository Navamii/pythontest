#Program to check if a number is even or odd.





num = int(input("Enter a number: "))

if num < 0 :

	print("Please enter positive integer only")
	
	exit()


 
if (num % 2) == 0 :
		print("{0} number is even".format(num))
else :
		print("{0} number is odd".format(num))
