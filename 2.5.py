print("Enter intgers. The function will go on until user inputs zero.")

count = 0
sum = 0.0
number = 1

while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1

if count == 0:
	print("Input some numbers.")
else:
	print("The average of the entered numbers are: ", sum / (count-1))
print("The sum of the entered numbers are: ", sum)