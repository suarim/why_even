numbers = [1,2,3,4,5,6,7,8,9]
target = 3
l=0
r=len(numbers)-1
while l<r:
    m=numbers[l]+numbers[r]
    if m==target:
        print([numbers[l],numbers[r]])
        break
    elif m<target:
        l+=1
    else:
        r-=1
