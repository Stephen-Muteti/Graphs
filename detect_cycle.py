from collections import deque


def undirected_cycle(start_node,parent,graph,vis):
	que = deque()
	vis[start_node] = 1
	que.append((start_node,parent))

	while que:
		node,parent = que[0]
		que.popleft()
		for adjNode in graph[node]:
			if not vis[adjNode]:
				vis[adjNode] = 1
				que.append((adjNode,node))
			elif not adjNode == parent: return True
	return False


def directed_cycle(start_node,graph,vis,pathVis):
	vis[start_node] = 1
	pathVis[start_node] = 1
	for adjNode in graph[start_node]:
		if not vis[adjNode]:
			if directed_cycle(adjNode,graph,vis,pathVis): return True
		elif pathVis[adjNode]:
			return True
	pathVis[start_node] = 0



if __name__ == '__main__':
	edges = [(0,1),(1,2),(2,3),(3,1),(3,4)]

	n = 5

	undirected_graph = [[]for i in range(5)]

	for u,v in edges:
		undirected_graph[u].append(v)
		undirected_graph[v].append(u)

	print(undirected_graph)
	vis = [0]*n

	found = False
	for node in range(n):
		if not vis[node]:
			if(undirected_cycle(node,-1,undirected_graph,vis)): 
				found = True
				break
	print(found)

	
	directed_graph = [[] for _ in range(n)]

	for u,v in edges:
		directed_graph[u].append(v)

	vis = [0]*n
	pathVis = [0]*n

	for node in range(n):
		if not vis[node]:
			if(directed_cycle(node,directed_graph,vis,pathVis)): print("True")