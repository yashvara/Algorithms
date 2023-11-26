import collections
def BFS(graph, root):
    visited = set()
    queue = collections.deque([root])
    visited.add(root)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for vert in graph[vertex]:
            if vert not in visited:
                visited.add(vert)
                queue.append(vert)
graph = {
    0: [1, 3, 4],
    1: [0, 2],
    2: [1, 3, 5],
    3: [0, 2, 4, 5],
    4: [0, 3, 6],
    5: [2, 3, 6],
    6: [4, 5]
}
root = 0
BFS(graph, root)


