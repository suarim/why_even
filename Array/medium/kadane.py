
l=[1,2,-5,4,5,-3,90]
msf=-9999
meh=0
cs=0
for i in l:
    meh+=i
    if meh<i:
        meh=i
        cs=i
    if msf<meh:
        msf=meh
        s=cs
        e=i
print(msf)
print(l[s-1:e])



def max_subarray(arr):
    best_sum = float('-inf')   # max‑so‑far
    cur_sum  = 0               # max‑ending‑here

    best_start = best_end = 0  # final sub‑array indices
    cur_start  = 0             # temp start index

    for i, x in enumerate(arr):
        # Either extend the current run or start fresh at i
        if cur_sum + x < x:
            cur_sum  = x
            cur_start = i
        else:
            cur_sum += x

        # Record a new best if we beat the previous best_sum
        if cur_sum > best_sum:
            best_sum   = cur_sum
            best_start = cur_start
            best_end   = i

    return best_sum, arr[best_start:best_end + 1]

# ─── Demo ─────────────────────────────────────────────
l = [1, 2, -5, 4, 5, -3, 90]
s, sub = max_subarray(l)
print(s)        # 96
print(sub)      # [4, 5, -3, 90]
