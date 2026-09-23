class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for t in tasks:
            count[ord(t) - ord('A')] += 1

        maxf = count[0]
        maxCount = 1
        for i in range(1, len(count)):
            if count[i] > maxf:
                maxCount = 1
                maxf = count[i]
            elif count[i] == maxf:
                maxCount += 1
        
        return max(
            len(tasks),
            (maxf - 1) * (n + 1) + maxCount
        )