class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        sub_sets = [set() for _ in range(9)]

        for x in range(9):
            for y in range(9):
                v = board[x][y]
                if v == '.':
                    continue

                if v in row_sets[y]:
                    return False
                else:
                    row_sets[y].add(v)
                
                if v in col_sets[x]:
                    return False
                else:
                    col_sets[x].add(v)
                
                sb = (y // 3) * 3 + (x // 3)
                if v in sub_sets[sb]:
                    return False
                else:
                    sub_sets[sb].add(v)

        return True