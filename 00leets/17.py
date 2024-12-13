map={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
digits="235"
comb=['']
for i in digits:
    sub=[]
    for c in comb:
        for x in map[i]:
            sub.append(c+x)
    comb=sub
print(comb)


map={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
res=['']
for i in "235":
    res=[x+y for x in res for y in map[i]]
print(res)