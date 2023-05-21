#Write a python program to Swap two tuples in Python
L=[]
L.append(tuple(input("Enter the first tuple: ").split(',')))
L.append(tuple(input("Enter the second tuple: ").split(',')))
print("The first tuple is: ",L[0])
print("The second tuple is: ",L[1])
L[0],L[1]=L[1],L[0]
print("After swapping the first tuple is: ",L[0])
print("After swapping the second tuple is: ",L[1])

