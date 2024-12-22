def minimumTotal(triangle):
    n=len(triangle)
    for rows in range(n-2,-1,-1):
        for cols in range(len(triangle[rows])):
            triangle[rows][cols]+=min(triangle[rows+1][cols],triangle[rows+1][cols+1])
    return triangle[0][0]
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

print(minimumTotal(triangle))