#Write a Python program to create a list of tuples from given list having number and its cube in each tuple. (e.g. (2,8),(3,27),....).

L=[]
L.append(tuple(input("Enter the first tuple: ").split(',')))
print("The tuple is: ",L[0])
L2=[]
for i in range(len(L[0])):
    L2.append((int(L[0][i]),int(L[0][i])**3))
print("The list of number and their cubes is: ",L2)