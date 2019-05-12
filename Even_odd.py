#Program to check if a number is even or odd.

while True:
 try:
  num = int(input("Enter a number: "))
  if num % 2 == 0 :
   print("{0} number is even".format(num))
  else :
   print("{0} number is odd".format(num))

 except ValueError:
    print("Oops!  That was no valid number.  Try again...")
 		
 if num < 0 :
    print("Please enter positive integer only")
	

 



