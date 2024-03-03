"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. 
In other words, any connected graph without simple cycles is a tree.
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where 
edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes 
ai and bi in the tree, you can choose any node of the tree as the root. 
When you select a node x as the root, the result tree has height h. 
Among all possible rooted trees, those with minimum height (i.e. min(h))  
are called minimum height trees (MHTs).
Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""

def findMinHeightTrees(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    if n == 1:
        return [0]

    graph = [[] for _ in range(n)]
    degrees = [0] * n
    
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1

    leaves = deque()
    for i in range(n):
        if degrees[i] == 1:
            leaves.append(i)

    remaining_nodes = n
    while remaining_nodes > 2:
        num_leaves = len(leaves)
        remaining_nodes -= num_leaves
        for _ in range(num_leaves):
            leaf = leaves.popleft()
            for neighbor in graph[leaf]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 1:
                    leaves.append(neighbor)

    return list(leaves)