class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            t = numbers[left] + numbers[right]
            if t == target:
                return [left + 1, right + 1]
            elif t < target:
                left += 1
            else:
                right -= 1
        
        return [-1, -1]