numCourses = 2
visited=[0]*numCourses
prerequisites = [[1,0],[0,1]]
graph = {i: [] for i in range(numCourses)}
for course, prereq in prerequisites:
    graph[course].append(prereq)
def dfs(node):
    if visited[node]==1:
        return False
    if visited[node]==2:
        return True
    visited[node]=1
    for i in graph[node]:
        if not dfs(i):
            return False
    visited[node]=2
    return True
for i in range(numCourses):
    if not dfs(i):
        print(False)
        exit()
print(True)