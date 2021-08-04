x = input("Enter 5 numbers ")
y=x.split()
print(y)
l2=y[::-1]
print("reversed list = ",l2)
l1=y[0:3]
print("sliced list= ",l1)
y[0]=0
print("replaced list-1 = ",y)
l1[0]=0
l1[-1]=0
print("replaced list-2 = ",l1)
