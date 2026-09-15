class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_map = {i:[] for i in range(n)}
        for node, neighbor in edges:
            adj_map[node].append(neighbor)
            adj_map[neighbor].append(node)

        visited = set()
        ans = 0

        def dfs(node):
            visited.add(node)
            for neighbor in adj_map[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            

        for node in range(n):
            if node not in visited:
                dfs(node)
                ans += 1

        return ans