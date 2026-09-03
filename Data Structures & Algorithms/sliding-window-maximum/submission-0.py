class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i in range(k-1):
            heapq.heappush(heap, (-nums[i], i))

        res = []
        l = 0
        for r in range(k-1, len(nums)):
            heapq.heappush(heap, (-nums[r], r))

            while heap[0][1] < l:
                heapq.heappop(heap)
            
            res.append(-heap[0][0])

            l += 1

        return res