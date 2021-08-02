numbers=input("Enter 5 numbers")
list1=numbers.split()
print(list1)
s=0
for n in list1:
    s = s + int(n)
print("sum = ",s)
