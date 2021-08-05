def main():
    y={}
    for i in range(number()):
        key=input("Enter key : ")
        value = input("Enter value :")
        y[key]=value
    print(y)
    sorted_values = sorted(y.values()) 
    dict1={}
    for i in sorted_values:
        for k in y.keys():
            if y[k] == i:
                dict1[k] = y[k]
                break

    print(dict1)
def number():
    n=int(input("Enter the number of elements in dictionary"))
    return n
main()
