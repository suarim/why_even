def PrintNto1backtrack(i,N):
    if i>N:
        return
    PrintNto1backtrack(i+1,N)
    print(i)
PrintNto1backtrack(1,10)