def insert_end(str):
	sub_str = str[-2:]
	print (sub_str * 4)

num=int(input("What is the length of the string ? : "))
print ("Type the words and press enter accordingly.")
for i in range(0, num):
    a = input("The word: ")
    insert_end(a)