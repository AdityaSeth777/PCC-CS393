
def make_sum(n):
  list1=[]
  for i in range(n):
   print("Enter the element: ")
   ele = int(input())
   list1.append(ele) # adding the element
   
  result = 0
  for x in list1:
   result = result + x
  return result

n = int(input("Enter the number of integers: "))
print("The sum of all the elements in the list are: ", make_sum(n))