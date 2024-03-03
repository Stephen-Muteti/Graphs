def dfs(node,graph,vis):
	vis[node] = True
	print(node, end=" ")
	for child in graph[node]:
		if not vis[child]:
			dfs(child,graph,vis)


def bfs(node,graph,vis):
	que = []
	que.append(node)
	while(que):
		cur = que[0]
		vis[cur] = True
		print(cur, end=" ")
		del que[0]
		for child in graph[cur]:
			if not vis[child]:
				que.append(child)
				vis[child] = True


if __name__ == '__main__':
	graph = [[1,2],[0,2,3],[0,1,3],[1,2],[5],[4]]

	n = len(graph)

	vis = [False]*n

	cmpts = 0
	for i in range(n):
		if not vis[i]:
			cmpts += 1
			dfs(i,graph,vis)

	print()
	print(f"components = {cmpts}")

	vis = [False]*n

	bfs(0,graph,vis)