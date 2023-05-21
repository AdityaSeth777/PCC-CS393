#Write a python program to Add Tuple to List and vice – versa.
L=[]
L.append(tuple(input("Enter the first tuple: ").split(',')))
print("The tuple is: ",L[0])
print("Enter the list: ")
L2=[]
while True:
    print("Enter the element: ")
    element=input()
    L2.append(element)
    
    y=input("Enter 'y' to continue or end to exit: ")
    if y!='y':
        break
print("The list is: ",L2)
L3=[]
L3=L2+list(L[0])
print("The new list is: ",L3)
L[0]=L[0]+tuple(L2)
print("The new tuple is: ",L[0])