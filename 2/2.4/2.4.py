lower_value = int(input ("Enter the Lowest Range Value: "))  
upper_value = int(input ("Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:
        for i in range (2, number):  
            if (number % i) == 0:
                break
        else:
            print (number)