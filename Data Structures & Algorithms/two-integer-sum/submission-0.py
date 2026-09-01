class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        paired = [(n, i) for i, n in enumerate(nums)]
        paired.sort()

        left = 0
        right = len(paired)-1

        while left < right:
            t = paired[left][0] + paired[right][0]
            if t == target:
                if paired[left][1] < paired[right][1]:
                    return [paired[left][1], paired[right][1]]
                else:
                    return [paired[right][1], paired[left][1]]
            elif t < target:
                left += 1
            else:
                right -= 1
        
        return [-1, -1]