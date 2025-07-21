def Print1toNbacktrack(i,N):
    if i<=0:
        return
    Print1toNbacktrack(i-1,N)
    print(i)
Print1toNbacktrack(10,10)