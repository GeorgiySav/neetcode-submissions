class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = {} # str : list
        palindromes[None] = None
        palindromes[''] = None

        def is_palindrome(ss):
            l, r = 0, len(ss)-1
            while l < r:
                if ss[l] != ss[r]:
                    return False
                l += 1
                r -= 1
            return True

        def part(ss):
            if ss in palindromes:
                return palindromes[ss]
            if len(ss) == 1:
                palindromes[ss] = [[ss]]
                return palindromes[ss]
            
            # iterate from start to finish, creating palindromes
            ps = []

            for i in range(len(ss)):
                if is_palindrome(ss[:i+1]):
                    sps = part(ss[i+1:])
                    if sps:
                        ps.extend([ss[:i+1]] + p for p in sps)
            if is_palindrome(ss):
                ps.append([ss])
            
            if len(ps) > 0:
                palindromes[ss] = ps
            else:
                palindromes[ss] = None
            return palindromes[ss]

        part(s)
        return palindromes[s]