l=int(input("length of the tromboloid"))
b=int(input("Breadth of the tromboloid"))
h=int(input("Height of the tromboloid"))
k=l**2+b**2+h**2
v=float((b**2*h**2)/k**.5)
print("volume of tromboloid",format(v,".3f"))
r=(v*3/(4*3.14))**(1/3)
print("radius",format(r,".3f"))
