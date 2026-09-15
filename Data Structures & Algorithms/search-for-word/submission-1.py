class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # traverse through the grid, dfs to search for neighbor with next character in string and if match, continue bfs from that point
        if not board or not word:
            return False

        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r,c, curr_c):
            # if reached word count iterations given requirements, return True
            if curr_c == len(word):
                return True

            # if any requirements fail, return false
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
            board[r][c] != word[curr_c] or (r,c) in visit):
                return False

            # add to visited in current dfs recursion
            visit.add((r,c))
            
            # recurse to neighbors
            found = (dfs(r+1, c, curr_c+1) or dfs(r-1, c, curr_c+1) or 
            dfs(r, c+1, curr_c+1) or dfs(r, c-1, curr_c+1))

            # backtrack and remove visited spaces for new dfs 
            visit.remove((r,c))

            return found


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True

        return False

    



