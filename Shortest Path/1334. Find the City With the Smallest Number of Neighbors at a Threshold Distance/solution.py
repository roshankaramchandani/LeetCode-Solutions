class Solution:
	def bfs(self, node: int, adj, maximum: int) -> int:
		heap = []
		heappush(heap,(0,node,-1))
		s = set()

		while heap:

			distance,curr,parent = heappop(heap)

			if distance > maximum:
				continue
			if curr in s:
				continue

			s.add(curr)

			for nextt,price in adj[curr]:
				if nextt != parent:
					heappush(heap,(distance+price,nextt,curr))

		return len(s) - 1



	def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
		adj = defaultdict(list)
		arr = [0]*n

		# to build the adjecency list
		for node_1, node_2, price in edges:
			adj[node_1].append((node_2,price))
			adj[node_2].append((node_1,price))

		# to iterate over thr nodes to get answer   
		for i in range(n):
			done = self.bfs(i,adj,distanceThreshold)
			arr[i] = done

		min_node = min(arr)
		ans = 0
		# calculate the reachable nodes from each index
		for i in range(len(arr)):
			if arr[i] == min_node:
				ans = i
		return ans