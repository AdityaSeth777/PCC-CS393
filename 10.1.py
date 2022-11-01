blogposts=[]
c=1
while c==1:
    d={}
    photos=int(input("Enter the number of photoes:"))
    comments=int(input("Enter the number of comments:"))
    likes=int(input("Enter the number of likes:"))
    shares=int(input("Enter the number of shares:"))
    if photos != 0:
       d["photos"]=photos
    if comments!=0:
       d["comments"]=comments
    if likes !=0 :
       d["likes"]=likes
    if shares !=0:
       d["shares"]=shares
    blogposts.append(d)
    print("Do you want to add more, enter 1\n")
    c=int(input())
print("The original blogpost:\n",blogposts)
total=0
for posts in blogposts:
     try:
          total=total+posts["likes"]
     except KeyError:
          posts["likes"]=0
print("The total likes in the blogpost:",total)
print("The changed blogpost is:\n",blogposts)


	
