def inp():
    return input("Enter three numbers")

z=inp().split()


p=int(z[0])
q=int(z[1])
r=int(z[2])

a=max(p,q,r)
print(a,"is the greatest number among ",p,",",q," and" ,r)
