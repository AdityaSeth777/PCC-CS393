# Opening a file
a=input("Enter the name of the file you want to open: ")
file = open(a, "r")
Counter = 0

# Reading from file
Content = file.read()
CoList = Content.split("\n")

for i in CoList:
	if i:
		Counter += 1

print("The number of lines in the file are -> ", Counter)
