bills=[5,5,10,10,50]
s=0
for i in bills:
    if i==5:
        s+=5
        print(s)
    else:
        if s>=i-5:
            s=s+(i-5)
            print(s)
        else:
            print(False)
            break
print(True)