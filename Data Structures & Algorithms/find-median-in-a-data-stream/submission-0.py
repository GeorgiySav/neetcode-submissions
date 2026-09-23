class MedianFinder:

    def __init__(self):
        self.lo = [] 
        self.hi = []

    def addNum(self, num: int) -> None:
        if len(self.lo) == len(self.hi): 
            heapq.heappush_max(self.lo, heapq.heappushpop(self.hi, num))
        else:
            heapq.heappush(self.hi, heapq.heappushpop_max(self.lo, num))

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (self.lo[0] + self.hi[0]) / 2
        else:
            return self.lo[0]