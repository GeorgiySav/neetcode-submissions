class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            heapq.heappush_max(heap, (x*x + y*y, [x, y]))
            if len(heap) > k:
                heapq.heappop_max(heap)
        
        return [p for d, p in heap]