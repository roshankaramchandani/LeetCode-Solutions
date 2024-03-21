class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i in range(len(equations)):
            start = equations[i][0]
            end = equations[i][1]
            val = values[i]

            if start in graph:
                graph[start].append((end,val))
            else:
                graph[start] = [(end,val)]
            if end in graph:
                graph[end].append((start,(1/val)))
            else:
                graph[end] = [(start,(1/val))]
        
        
        
        def solve(start,end):
            if start==end and start in graph:
                return 1.0
            ans = 1
            visited = set()
            q = deque([(start,1)])
            while q:
                curr,currVal = q.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                if curr == end:
                    return currVal
                for neighbor,val in graph[curr]:
                    q.append((neighbor,currVal*val))
            return -1.0
        
        ans = []
        for start,end in queries:
            if start in graph and end in graph:
                ans.append(solve(start,end))
            else:
                ans.append(-1.0)
        return ans
                    
