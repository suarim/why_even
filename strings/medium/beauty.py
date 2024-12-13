s = "aabcbaa"
stack = []
res = []

def calculate_beauty(substring):
   
    freq = {}
    for char in substring:
        freq[char] = freq.get(char, 0) + 1
    max_freq = max(freq.values())
    min_freq = min(freq.values())
    return max_freq - min_freq

def dfs(stack, lens):
    
    if len(stack) == lens:
        substring = ''.join(n for n, _ in stack)
        beauty = calculate_beauty(substring)
        if beauty > 0: 
            res.append(substring)
        return
    
    for i, n in enumerate(s):
        if (n, i) not in stack:  
            stack.append((n, i))  
            dfs(stack, lens)      
            stack.pop()           


for length in range(1, 5):
    dfs(stack, length)


print(res)
