def Print1toN(i,N):
    if i<=0:
        return
    print(i)
    Print1toN(i-1,N)
Print1toN(100,100)