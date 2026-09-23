class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        perms = [] 
        for i, n in enumerate(nums):
            perms.extend([
                [n] + p
                for p in self.permute(nums[:i] + nums[i+1:])
            ])

        return perms