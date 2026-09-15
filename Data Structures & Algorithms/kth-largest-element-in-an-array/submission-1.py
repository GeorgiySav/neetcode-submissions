class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(l, r):
            p = r
            i, j = l, r-1

            while i <= j:
                if nums[i] > nums[p]:
                    i += 1
                elif nums[j] < nums[p]:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[i], nums[p] = nums[p], nums[i]            

            return i
        
        l, r = 0, len(nums)-1
        while True:
            p = partition(l, r)
            if p == (k-1):
                return nums[p]
            if p < (k-1):
                l = p+1
            else:
                r = p-1
        return 0