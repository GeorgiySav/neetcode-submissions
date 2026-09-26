class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        def contains(x, y, s):
            if (x, y) in seen or not (
                0 <= x < len(board) and 0 <= y < len(board[0])
            ):
                return False
            if word[s] == board[x][y]:
                if s == len(word)-1:
                    return True

                seen.add((x, y))
                for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if contains(i, j, s+1):
                        return True 
                seen.remove((x, y))
            return False

        for x in range(len(board)):
            for y in range(len(board[0])):
                if contains(x, y, 0):
                    return True
        return False