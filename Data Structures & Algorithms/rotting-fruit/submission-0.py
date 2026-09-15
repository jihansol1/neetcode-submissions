class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        fresh_fruits = 0
        minutes = 0

            
        q = collections.deque()

        # traverse through grid to add the rotten fruits to queue and count fresh fruits
        for r in range(rows):
            for c in range(cols):
                # add rottent to queue
                if grid[r][c] == 2:                    
                    q.append((r,c))
                # count fresh fruits
                if grid[r][c] == 1:
                    fresh_fruits += 1


        directions = [[1,0],[-1,0],[0,-1],[0,1]]    

        while fresh_fruits > 0 and q:
            for _ in range(len(q)):
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        # turn fresh adjacent fruit to rotten fruit
                        grid[r][c] = 2
                            # append new rotten fruit to queue
                        q.append((r,c))
                        fresh_fruits -= 1

            minutes += 1

        return minutes if fresh_fruits == 0 else -1

        
        