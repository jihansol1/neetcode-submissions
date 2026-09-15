class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_seen = defaultdict(set)
        col_seen = defaultdict(set)
        box_seen = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in row_seen[i]
                    or board[i][j] in col_seen[j] 
                    or board[i][j] in box_seen[(i//3,j//3)]):
                    return False

                row_seen[i].add(board[i][j])
                col_seen[j].add(board[i][j])
                box_seen[(i//3, j//3)].add(board[i][j])

        return True

                