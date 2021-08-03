def main():
    a = input_number()
    b = input_number()
    summation = add(a, b)
    display(a, b, summation)

def input_number():
    return int(input("Enter an integer"))
    
def display(x,y,z):
    print(x,y,z)
     
def add(x,y):
    s=x+y
    return s
     
main()

