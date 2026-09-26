class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        nums.sort()

        def dfs(buffer, i):
            if i == len(nums):
                subsets.add(tuple(buffer))
                return
            
            dfs(buffer, i+1)
            dfs(buffer + [nums[i]], i+1)

        dfs([], 0)
        return [list(s) for s in subsets]