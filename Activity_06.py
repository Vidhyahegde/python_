x=map(int,input("Enter five integers ").split())
y=list(x)
z=y[::-1]
print("reversed list = ",z)
l1=y[0:3]
print("sliced list = ",l1)
y[0],y[-1],l1[-1],l1[0]=0,0,0,0
#y[0] = y[-1] = 0
print("replace list1 = ",y)
print("replace list2 = ",l1)
