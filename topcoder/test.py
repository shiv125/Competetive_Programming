from collections import deque

def BFS(start, end):
    """ Method to determine if a pair of vertices are connected using BFS

    Args:
      start, end: vertices for the traversal.

    Returns:
      [start, v1, v2, ... end]
    """
    path = []
    q = deque()
    q.append(start)
    while len(q):
      tmp_vertex = q.popleft()
      if tmp_vertex not in path:
        path.append(tmp_vertex)

      if tmp_vertex == end:
        return path.append()

      for vertex in graph[tmp_vertex]:
        if vertex not in path:
          q.append(vertex)
'''
graph = {'A': ['B', 'C','E'],
           'B': ['A','C', 'D'],
           'C': ['D'],
           'D': ['C'],
           'E': ['F','D'],
           'F': ['C']}
'''
graph={0:[2,3],1:[2,3],2:[0,1],3:[0,1]}
print BFS(0,1)
