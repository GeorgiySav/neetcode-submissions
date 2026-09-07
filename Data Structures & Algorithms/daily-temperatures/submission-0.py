class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = deque()

        for j, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                i = stack.pop()
                res[i] = j - i
            
            stack.append(j)
        
        return res