class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src,dst,time in times:
            graph[src].append((time,dst))
        

        ans = {}
        heap = [[0,k]]

        while heap:
            currTime,currNode = heapq.heappop(heap)
            if currNode in ans:
                continue
            ans[currNode] = currTime
            for nextTime,nextNode in graph[currNode]:
                if nextNode not in ans:
                    heapq.heappush(heap, [currTime+nextTime,nextNode])
            
        if len(ans)!=n:
            return -1
        return max(ans.values())                