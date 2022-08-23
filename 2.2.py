number = int(input ("Enter the number of which the user wants to print the multiplication table: "))  
# iterate mul 10 times
print ("The Multiplication Table of", number," ")
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)