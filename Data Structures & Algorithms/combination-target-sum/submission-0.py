class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]

        sums = []

        for i, n in enumerate(nums):
            t = 1
            while (t * n) <= target:
                subs = self.combinationSum(nums[i+1:], target - (t * n))
                for s in subs:
                    sums.append(
                        ([n] * t) + s
                    )
                t += 1

        return sums 