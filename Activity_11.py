def main():
    a = int(input())
    b = int(input())
    def add(x,y):
        s=x+y
        return s
    summation = add(a, b)
    def display(x,y,z):
        print(x,y,z)
    display(a, b, summation)



main()
