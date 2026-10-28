class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = set()
        def dfs(total, i):
            if (total, i) in cache:
                return False

            if i == len(nums):
                return total == 0
            
            if dfs(total + nums[i], i+1):
                return True
            if dfs(total - nums[i], i+1):
                return True

            cache.add((total, i))
            return False
        
        return dfs(nums[0], 1)