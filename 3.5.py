#Works for multi line input.
s=input("Enter the string: ")
l=[]
l=s.split(".")
ps=input("Enter the prefix string: ")
for i in range(len(l)-1):
    print(ps+l[i],end=".")
else:
    print(l[len(l)-1])

