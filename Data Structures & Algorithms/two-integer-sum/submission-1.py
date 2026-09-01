class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        imap = {}

        for i, n in enumerate(nums):
            if target-n in imap:
                return [imap[target-n], i]
            else:
                imap[n] = i
        
        return None