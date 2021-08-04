x = input('enter the elements')
y = x.split()
for i in range(0, len(y)):
    y[i] = int(y[i])
z=y[::-1]
print("reversed list = ",z)
l1=y[0:3]
print("sliced list = ",l1)
y[0]=0
y[-1]=0
print("replace list1 = ",y)
l1[0]=0
l1[-1]=0
print("replace list2 = ",l1)



