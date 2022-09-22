# open both files
a=input("Enter the name of the file you want to open: ")
b=input("Enter the name of the file you want to open: ")
with open(a,'r') as firstfile, open(b,'a') as secondfile:
	
	# read content from first file
	for line in firstfile:
			
			# append content to second file
			secondfile.write(line)
print("Copied successfully.")
