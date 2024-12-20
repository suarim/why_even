l = []

def ins(v):
    if len(l) < 7:
        l.append(v)
    else:
        print("Stack is full")

def rem():
    if len(l) == 0:
        print("Stack is empty")
    else:
        l.pop()

def peek():
    return l[-1] if l else None

def prints():
    print(l)

ins(1)
ins(2)
ins(3)
ins(4)
ins(4)
ins(4)
ins(4)
ins(4)
ins(4)
ins(4)
ins(4)
ins(4)
ins(4)
ins(4)
ins(4)
prints()
ins(4)
ins(4)
ins(4)
prints()
prints()
prints()
rem()
rem()
rem()
rem()
rem()
rem()
prints()
