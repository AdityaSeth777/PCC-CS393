
n=int(input("Enter the number of students: "))
for i in range(n):
        name=input("Enter the name of the student: ")
        assignment=[]
        test=[]
        lab=[]
        for j in range(4):
                assignment.append(int(input("Enter the assignment marks: ")))
        for j in range(2):
                test.append(int(input("Enter the test marks: ")))
        for j in range(2):
                lab.append(float(input("Enter the lab marks: ")))
        d={}
        d["name"]=name
        d["assignment"]=assignment
        d["test"]=test
        d["lab"]=lab
        print("The dictionary is: ",d)
        avg=(sum(assignment)/4*0.1)+(sum(test)/2*0.7)+(sum(lab)/2*0.2)
        print("The average marks of ",name," is: ",avg)
        if(avg>=90):
                print("The letter grade of ",name," is: A")
        elif(avg>=80):
                print("The letter grade of ",name," is: B")
        elif(avg>=70):

                print("The letter grade of ",name," is: C")
        else:
                print("The letter grade of ",name," is: D")
        print("\n")

