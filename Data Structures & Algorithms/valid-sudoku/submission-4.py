class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # row
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] in row_set:
                    return False
                if board[i][j] == ".":
                    continue
                row_set.add(board[i][j])

        # col
        for i in range(9):
            col_set = set()
            for j in range(9):
                if board[j][i] in col_set:
                    return False
                if board[j][i] == ".":
                    continue
                col_set.add(board[j][i])

        # sub-box

        for square in range(9):
            square_set = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in square_set:
                        return False
                    if board[row][col] == ".":
                        continue
                    square_set.add(board[row][col])

        return True