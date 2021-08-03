def volume(l,b,h):
    def div(a,b):
        q=float(a/b)
        return q
    def den(l,b,h):
        k=float((l**2+b**2+h**2)**.5)
        return k
   
    s=float(b**2*h**2)
    v=div(s,den(l,b,h))
    return v 
def main():
    l=int(input("Enter the length:"))
    b=int(input("Enter the breadth:"))
    h=int(input("ENter the height:"))
    print("Volume of the tromboloid is",format(volume(l,b,h),".3f"))
main()
