class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort()

        prev_idx, idx = 0, 0

        for i in range(len(nums)):
            idx = prev_idx if i > 0 and nums[i] == nums[i-1] else 0
            prev_idx = len(subsets)
            for j in range(idx, prev_idx):
                tmp = subsets[j].copy()
                tmp.append(nums[i])
                subsets.append(tmp)

        return subsets