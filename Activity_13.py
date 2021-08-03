def prime_no(n):
    for i in (1,n):
        if (n%i!=0):
            print(n,"is a prime number")
            break
        elif(n==2):
            print(n,"is the only even prime number")
            break
        elif(n==1):
            print(n,"is neither prime nor compposite")
            break
        else:
            print(n,"is not a prime number")
            break
x=int(input("Enter a number"))
prime_no(x)
