a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c = a+b
print("%d+%d=%d"%(a,b,c))
print("{}+{}={}".format(a,b,c))
print(str(a)+'+'+str(b)+'='+str(c))
print(*[a,'+',b,'=',c])
