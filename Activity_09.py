l=float(input("length of the tromboloid - "))
b=float(input("Breadth of the tromboloid - "))
h=float(input("Height of the tromboloid - "))
k=l**2+b**2+h**2
v=(b**2*h**2)/k**.5
print("volume of tromboloid ",format(v,".3f"))
r=(v*3/(4*3.14))**(1/3)
print("radius ",format(r,".3f"))
