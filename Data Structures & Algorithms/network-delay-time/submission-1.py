class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for ui, vi, ti in times:
            adj[ui].append((vi, ti))
        
        priority_queue = [(0, k)]
        visit = set()
        t = 0

        while priority_queue:
            t1, n1 = heapq.heappop(priority_queue)
            if n1 in visit:
                continue
            
            visit.add(n1)
            t = t1

            for n2, t2 in adj[n1]:
                heapq.heappush(priority_queue, (t1 + t2, n2))
        return t if len(visit) == n else -1