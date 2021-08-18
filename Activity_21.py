def main():
    import time
    sec = time.time()
    m=sec/60
    h=m/60
    d=h/24
    y=round(d//365)
    ry=d%365
    rm=round(ry//30)
    rd=round(d%30)
    print ("Years passed since -",y)
    print ("Months passed since -",rm)
    print ("Days passed since -",rd)
    print ("Today's date -",rd+1,'/',rm,'/',1970+y)

main()
