def number():
    return input("Enter the number- ")
def project():
    dict_={1:'', 2:'ABC', 3:'DEF', 4:'GHI', 5:'JKL', 6: 'MNO', 7: 'PQRS',
           8: 'TUV', 9: 'WXYZ', 0:''}
    x=number()
    y=string_obt(dict_,x,len(x))
    display(y)

def string_obt(dict_,num,n):
    a=''
    b=[""]
    for i in range (0,len(num)):
        count=1
        if i+1!=len(num):
            while num[i]==num[i+1]:
                count+=1
                i+=1
                if i+1==len(num):
                    break
        c=[]
        a=lists(dict_[int(num[i])], count)
        for k in b:
            for j in a:
                c.append(k + j)
        c=list(set(c))
        b=c
        i+=1
    return b
def lists(cha, count):
    lis = comb_list(cha, count)
    if count < 3:
        return [lis[i] for i in range(count)]
    elif count == 3 or (len(cha) == 4 and count == 4):
        return lis
    else:
        lis1 = []
        if(len(cha) == 3):
            lis2 = poss_list(cha, count - 3)
        else:
            lis2 = poss_list(cha, count - 4)
        for i in lis:
            for j in lis2:
                lis1.append(i+j)
                lis1.append(j+i)
        return list(set(lis1))

def comb_list(cha, count):
    lis = []
    if count == 1:
        return cha[0]
    elif count == 2:
        lis = cha[0] * 2, cha[1] 
        return lis
    elif((len(cha) == 3 and count >= 3) or (len(cha) == 4 and count == 3)):
        lis.append(cha[0] * 3)
        lis.append(cha[0]+cha[1])
        lis.append(cha[1]+cha[0])
        lis.append(cha[2])
        return lis
    else:
        lis.append(cha[0] * 4)
        lis.append((cha[0] * 2) + cha[1])
        lis.append(cha[1] + (cha[0] * 2))
        lis.append(cha[0] + cha[1] + cha[0])
        lis.append(cha[1] * 2)
        lis.append(cha[0] + cha[2])
        lis.append(cha[2] + cha[0])
        lis.append(cha[3])
        return lis

def display(ans):
    i = 0
    while i < len(ans) - 1:
        print(ans[i], end = ", ")
        i += 1
    print("The possible strings are",ans[i])
project()
