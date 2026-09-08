class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _subsets(i):
            if i == len(nums):
                return [[]]
            
            subsets = _subsets(i+1)
            l = len(subsets)
            subsets.extend([nums[i]] + s for s in subsets[:l])

            return subsets
 
        return _subsets(0)