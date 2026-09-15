class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0


        def bfs(r,c):
            area = 0
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            area += 1

            while q:
                row, col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr, dc in directions:
                    r, c = dr+row, dc+col
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
                        area += 1

            return area




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    max_area = max(max_area, area)

        return max_area