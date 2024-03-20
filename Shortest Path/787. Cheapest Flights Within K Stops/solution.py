class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s,d,price in flights:
            graph[s].append((d,price))
        

        dist = [math.inf]*n
        dist[src] = 1
        q = deque([(src,0)])

        while q and k>=0:
            for _ in range(len(q)):
                curr,currPrice = q.popleft()

                for neighbor,nextPrice in graph[curr]:
                    newPrice = currPrice + nextPrice
                    if newPrice<dist[neighbor]:
                        dist[neighbor] = newPrice
                        q.append((neighbor,newPrice))
            k -= 1
        

        return dist[dst] if dist[dst]!=math.inf else -1