lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	
print(lst)
pos_count, neg_count = 0, 0
 
# iterating each number in list
for num in lst:
     
    # checking condition
    if num >= 0:
        pos_count += 1
 
    else:
        neg_count += 1
         
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)