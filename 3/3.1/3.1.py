
s=input("Enter the string: ")
def mid(str):
    i=len(str)//2
    c=input("Enter the string to be inserted in the middle: ")
    ms=str[:i]+c+str[i:]
    print("The modified string is: ",ms)
mid(s)
