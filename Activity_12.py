def inp():
    return input("Enter three numbers - ")
     
def main():
    x=inp()
    y=x.split()
    z=list(y)
    p=int(z[0])
    q=int(z[1])
    r=int(z[2])
    m=ma(p,q,r)
    print(m,"is the greatest number among ",p,",",q," and" ,r)
def ma(p,q,r):
    if p>q and p>r:
        return p
    elif q>p and q>r:
        return q
    else:
        return r
main()
