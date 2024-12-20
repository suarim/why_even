st=[]
def add(x):
    if len(st)==0:
        st.append((x,x))
    else:
        cmin=min(x,st[-1][1])
        st.append((x,cmin))
def remove():
    if st:
        return st.pop()
def getmin():
    if st:
        return st[-1][1]
    return None
def peek():
    if st:
        return st[-1][0]
    return None
add(1)
add(2)
add(3)
add(4)
print(getmin())
add(0)
print(getmin())
print(remove())
print(getmin())