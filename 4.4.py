lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	
print(lst)

# Removing duplicates from the list
list2 = list(set(lst))

# Sorting the list
list2.sort()

# Printing the second last element
print("Second largest element is:", list2[-2])
