def blah(c):
    if c<1:
        return 
    blah(c-1)
    print(c)
blah(10)
