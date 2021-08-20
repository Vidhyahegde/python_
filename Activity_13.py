def prime_no(n):
    if n==1:
        print("Neither prime nor composite")
        return
    if n==2:
        print(n," is the only even prime number")
        return
    
    
    for i in range(2,int(n**.5)+1):
        if (n%i==0):
            print(n,"is not a prime number")
            break
    else:
        print(n," is a prime number")
    
            
def main():
    x = number()
    prime_no(x)

def number():
    return int(input("Enter a number - "))

main()

