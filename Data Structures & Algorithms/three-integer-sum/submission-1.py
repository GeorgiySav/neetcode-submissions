class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def twosum(target, left):
            l = left
            r = len(nums) - 1
            twos = []

            while l < r:
                t = nums[l] + nums[r]
                if t == target:
                    twos.append([nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif t < target:
                    l += 1
                else:
                    r -= 1
            
            return twos
        
        triples = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            twos = twosum(0 - nums[i], i+1)
            triples.extend([nums[i]] + t for t in twos)
        
        return triples