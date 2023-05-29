
n=int(input("Enter the number of elements in the dictionary: "))
d={}
for i in range(n):
     key=input("Enter the key: ")
     value=input("Enter the value: ")
     d[key]=value
print("The dictionary is: ",d)
print("The sorted dictionary by key is: ",sorted(d.items()))
print("The sorted dictionary by value is: ",sorted(d.items(),key=lambda x:x[1]))