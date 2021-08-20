def input():
    x=input("Enter three numbers - ")
    z=x.split()
    p=int(z[0])
    q=int(z[1])
    r=int(z[2])
    return p,q,r 
def main():
    p,q,r= input()
    m=maximim(p,q,r)
    print(m," is the greatest number among ",p,",",q," and " ,r)
def maximum(p,q,r):
    if p>q and p>r:
        return p
    elif  q>r:
        return q
    else:
        return r
main()
