#Input two tuples and write a python program to find Modulo of tuple elements and store in a third tuple.

L=[]
L.append(tuple(input("Enter the first tuple: ").split(',')))
L.append(tuple(input("Enter the second tuple: ").split(',')))
if len(L[0])!=len(L[1]):
    print("The tuples are not of equal length")
else:
    print("The first tuple is: ",L[0])
    print("The second tuple is: ",L[1])
    L3=[]
    for i in range(len(L[0])):
        L3.append(int(L[0][i])% int(L[1][i]))
    print("The new tuple is: ",tuple(L3))