'''
Prim's Algorithm to find minimum spanning tree on network represented as adjacency list

Source: 
FreeCodeCamp - Graph Algorithms in Python: BFS, DFS, and Beyond 
'''


import heapq

def prim(graph, start_node):
    mst = []
    visited = {start_node}
    edges = [(w, start_node, to_node) for to_node, w in graph[start_node]] 
    heapq.heapify(edges) 

    while edges:
        weight, from_node, to_node = heapq.heappop(edges) 
        if to_node not in visited:
            visited.add(to_node)
            mst.append((from_node, to_node, weight)) 
            for next_node, w in graph[to_node]:    
                if next_node not in visited:
                    heapq.heappush(edges, (w, to_node, next_node))
    return mst
