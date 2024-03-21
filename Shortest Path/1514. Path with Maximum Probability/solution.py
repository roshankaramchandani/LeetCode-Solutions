class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            src = edges[i][0]
            dst = edges[i][1]
            prob = -succProb[i]

            graph[src].append([prob,dst])
            graph[dst].append([prob,src])

        heap = [[1,start_node]]
        ans = {}

        while heap:
            currProb,currNode = heapq.heappop(heap)
            if currNode in ans:
                continue

            ans[currNode] = abs(currProb)

            for nextProb,nextNode in graph[currNode]:
                 if nextNode not in ans:
                    heapq.heappush(heap, [-abs(currProb*nextProb),nextNode])
            
        return ans[end_node] if end_node in ans else 0



