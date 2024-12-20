def soln(image,sr,sc,color):
    def dfs(image,sr,sc,color,visited):
        visited[sr][sc]=1
        image[sr][sc]=color
        directions=[(0,1),(0,-1),(1,0),(-1,0)]  
        for i,j in directions:
            dx,dy=sr+i,sc+j
            if 0<=dx<len(image) and 0<=dy<len(image[0]) and image[dx][dy]==1 and visited[dx][dy]==0:
            
                dfs(image,dx,dy,color,visited)
    visited=[[0]*len(image[0]) for i in range(len(image))]
    dfs(image,sr,sc,color,visited)
    return image


image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0

print(soln(image,sr,sc,color))