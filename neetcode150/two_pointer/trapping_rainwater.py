height = [0,2,0,3,1,0,1,3,2,1]
maxl=0
maxr=0
tp=0
hl=[0 for i in range(len(height))]
hr=[0 for i in range(len(height))]
for i in range(len(height)):
    maxl=max(maxl,height[i])
    hl[i]=maxl
for i in range(len(height)-1,-1,-1):
    maxr=max(maxr,height[i])
    hr[i]=maxr
print(hr)
for i in range(len(height)):
    tp+=min(hl[i],hr[i])-height[i]
print(tp)