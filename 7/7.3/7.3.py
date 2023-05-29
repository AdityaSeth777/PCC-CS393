def string_test(s):
    d={"up_CASE":0, "low_CASE":0}
    for c in s:
        if c.isupper():
           d["up_CASE"]+=1
        elif c.islower():
           d["low_CASE"]+=1
        else:
           pass
    print ("Entered String -> ", s)
    print ("No. of upper case characters -> ", d["up_CASE"])
    print ("No. of lower case Characters -> ", d["low_CASE"])

a=input("Enter the string: ")
string_test(a)