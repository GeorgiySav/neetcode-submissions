class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        d_to_s = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        } 

        combs = []

        def backtrack(i, c):
            if i == len(digits):
                combs.append(c)
                return
            
            for char in d_to_s[digits[i]]:
                backtrack(i+1, c + char)
        
        backtrack(0, '')
        return combs