'''
The code below assigns the 5th letter of each word in 'food' to the new list fifth. However, the code currently produces errors. Insert a try/except clause that will allow the code to run and produce a list of the 5th letter in each word. If the word is not long enough, it should not print anything out. Note: The 'pass' statement is a null operation; nothing will happen when it executes.

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]

fifth = []

for x in food:

    fifth.append(x[4])
'''
l=list(map(str,input("Enter the words:").split()))
print("The list of food is: ",l)
fifth=[]
for f in l:
    try:
       fifth.append(f[4])
    except IndexError:
       continue
print("The list carrying fifth letters of each word is: ",fifth)
