class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min, cur_max = 1, 1
        for n in nums:
            new_n = cur_max * n
            cur_max = max(new_n, n, cur_min * n)
            cur_min = min(new_n, n, cur_min * n)
            res = max(res, cur_max)
        return res
