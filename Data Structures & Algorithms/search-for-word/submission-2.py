class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def contains(x, y, s):
            if not (
                0 <= x < len(board) and 0 <= y < len(board[0])
            ) or board[x][y] == '#':
                return False

            if word[s] == board[x][y]:
                if s == len(word)-1:
                    return True

                board[x][y] = '#'
                for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if contains(i, j, s+1):
                        return True 
                board[x][y] = word[s]
            return False

        for x in range(len(board)):
            for y in range(len(board[0])):
                if contains(x, y, 0):
                    return True
        return False