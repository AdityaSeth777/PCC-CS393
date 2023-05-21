
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	print ("Enter the element: ")
	ele = int(input())
	lst.append(ele) # adding the element
	
print(lst)

l = []  # empty list
 
# checking if elements present in the list or not
for i in lst:
    # reversing the list
    l.insert(0, i)
# printing result
print(l)
