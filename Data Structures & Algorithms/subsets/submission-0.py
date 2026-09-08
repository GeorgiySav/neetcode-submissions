class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = [[]]

        def _subsets(i):
            if i == len(nums):
                return [[]]
            
            subsets = []
            subsubsets = _subsets(i+1)
            subsets.extend(subsubsets)
            subsets.extend([nums[i]] + s for s in subsubsets)

            return subsets
 
        return _subsets(0)