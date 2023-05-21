# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	print("Enter the element: ")
	ele = int(input())
	lst.append(ele) # adding the element
	
print(lst)
def swapList(lst):
    size = len(lst)
     
    # Swapping
    temp = lst[0]
    lst[0] = lst[size - 1]
    lst[size - 1] = temp
     
    return lst
     
 
print(swapList(lst))
