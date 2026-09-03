class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ']})':
                for ps, pc in [('(', ')'), ('[', ']'), ('{', '}')]:
                    if c == pc:
                        if stack and stack[-1] == ps:
                            stack.pop()
                        else:
                            return False
            else:
                stack.append(c)
        
        return len(stack) == 0
                