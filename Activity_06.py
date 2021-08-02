x = input("Enter 5 numbers")
y=x.split()
list1=list(y)
print(list1)
l1=list1[0:3]
print("sliced list=",l1)
list1[-1]=0
list1[0]=0
print("replaced list-1 =",list1)
l1[0]=0
l1[-1]=0
print("replaced list-2 =",l1)
