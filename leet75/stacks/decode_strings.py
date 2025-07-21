s="3[a4[bc]]"
# abcbcbcbc
l=[]
curnum=0
curstr=""
prevstr=""
for i in s:
    if i == "[":
        l.append(curstr)
        l.append(curnum)
        curstr=""
        curnum=0
    elif i == "]":
        num=l.pop()
        strr=l.pop()
        curstr=strr+num*curstr
    elif i.isdigit():
        curnum=curnum*10+int(i)
    else:
        curstr+=i
print(curstr)