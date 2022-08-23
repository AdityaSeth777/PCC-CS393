lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	
print(lst)
even_count, odd_count = 0, 0
num = 0
 
# using while loop    
while(num < len(lst)):
     
    # checking condition
    if lst[num] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
     
    # increment num
    num += 1
     
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)