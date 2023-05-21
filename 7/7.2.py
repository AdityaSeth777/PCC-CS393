
def multiplyList(myList):
	# Multiply elements one by one
	result = 1
	for x in myList:
		result = result * x
	return result

list1 = []
# number of elements as input in List1
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
	print("Enter the element: ")
	ele = int(input())
	list1.append(ele) # adding the element


print("The product of all the elements in the list are: ", multiplyList(list1))
