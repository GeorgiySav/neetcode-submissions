class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            d = abs(x - y)
            if d != 0:
                heapq.heappush_max(stones, d)
        
        if stones:
            return stones[0]
        else:
            return 0