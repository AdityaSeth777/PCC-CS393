
def maximum(a, b, c):

	if (a >= b) and (a >= c):
		largest = a

	elif (b >= a) and (b >= c):
		largest = b
	else:
		largest = c
		
	return largest


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print("The greatest number is:", maximum(a, b, c))
