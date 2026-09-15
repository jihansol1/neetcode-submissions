class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # need to check the rows if it has duplicates or has vals from 1 to 9
        # need to check the cols if it has duplciates or vals from 1 to 9
        # how can we check the sub boxes?
        

        # check the rows
        for row in range(9):
            row_dups = set()
            for j in range(9):
                if board[row][j] == '.':
                    continue
                if board[row][j] in row_dups:
                    return False
                row_dups.add(board[row][j])
        
        # check the cols
        for col in range(9):
            col_dups = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in col_dups:
                    return False
                col_dups.add(board[i][col])

        # check the sub spaces
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True




