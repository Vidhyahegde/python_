def main():
    y={}
    for i in range(number()):
        key=input("Enter key:")
        value = input("Enter value :")
        y[key]=value
    print(y)
    from collections import OrderedDict
    dict1 = OrderedDict(sorted(y.items()))
    print(dict(dict1))

        
def number():
    n=int(input("Numberof elements in the dictionary"))
    return n
main()
