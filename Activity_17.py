def inp():
    a=input("Enter the list of tuples here -")
    b=a.replace("'",'')    
    return b
    
    
def string1(a):
    b=str()
    for i in a.split('), ('):
        c=i.split(',')
        b=b+c[0]+"="+c[1]+"; "
        b=b.rstrip(';')
    b=b.replace('[(','')
    b=b.replace(')]','')
    return b

y=inp()
x=string1(y)
print(x)


