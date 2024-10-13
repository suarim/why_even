s="((()))("
stack=[]
for i in s:
    if i in "([{":
        stack.append(i)
    else:
        if not stack:
            print(False)
        else:
            if i==")" and stack[-1]!="(":
                print(False)
                exit()
            elif i=="]" and stack[-1]!="[":
                print(False)
                exit()
            elif i=="}" and stack[-1]!="{":
                print(False)
                exit()
            stack.pop()
print(len(stack)==0)