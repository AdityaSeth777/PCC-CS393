#Write a python program to Copy specific elements from one tuple to a new tuple
L=[]
L.append(tuple(input("Enter the first tuple: ").split(',')))

print("The first tuple is: ",L[0])
print("Enter the elements you want to copy: ")
L2=[]
while True:
    print("Enter the element: ")
    element=input()
    
    if element not in L[0]:
        print("Enter the correct element: ")
        element=input()
    
    L2.append(element)

    y=input("Enter 'y' to continue or end to exit: ")
    if y != "y":
        break
print("The new tuple is: ",tuple(L2))