def sum1(i,N):
    if i>N:
        return 0
    return i+sum1(i+1,N)
print(sum1(1,5))