s="()[{}()"
st=[]
for i in range(len(s)):
    if s[i] in "({[":
        st.append(s[i])
    else:
        if len(st)==0:
            print("Invalid")
            exit()
        if s[i]==")" and st[-1]!="(":
            print("Invalid")
            exit()
        if s[i]=="}" and st[-1]!="{":
            print("Invalid")
            exit()
        if s[i]=="]" and st[-1]!="[":
            print("Invalid")
            exit()
        st.pop()
print(len(st)==0)
