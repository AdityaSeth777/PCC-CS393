def check(s1, s2):
	
	if(sorted(s1)== sorted(s2)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")		
		
s1 =input("Enter the first string: ")
s2 =input("Enter the second string: ")
check(s1, s2)