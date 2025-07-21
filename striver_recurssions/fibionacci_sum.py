def fibsum(i):
    if i<=1:
        return i
    return fibsum(i-1)+fibsum(i-2)
print(fibsum(3))