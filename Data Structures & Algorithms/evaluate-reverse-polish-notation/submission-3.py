class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for t in tokens:
            if t == '+':
                r = stack.pop()
                l = stack.pop()
                stack.append(int(r + l)) 
            elif t == '-':
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l - r))
            elif t == '*':
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l * r)) 
            elif t == '/':
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l / r)) 
            else:
                stack.append(int(t))
        
        return stack[-1]