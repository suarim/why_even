def Print1toN(i,N):
    if i>N:
        return
    print(i)
    Print1toN(i+1,N)
Print1toN(1,100)