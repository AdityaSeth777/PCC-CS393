word=input("Enter the word: ")
count = 0
a=input("Enter the name of the file you want to open: ")

with open(a, 'r') as f:
	for line in f:
		words = line.split()
		for i in words:
			if(i==word):
				count=count+1
print("Occurrences of the word", word, ":", count)