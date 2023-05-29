
test_str=input("Enter the string: ")
repl_dict={}
n=int(input("Enter the number of elements in the dictionary: "))
for i in range(n):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    repl_dict[key]=value
for key in repl_dict:
    test_str=test_str.replace(key,repl_dict[key])
print("The string is: ",test_str)
