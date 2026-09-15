class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_map = {i:[] for i in range(n)}
        for node, neighbor in edges:
            adj_map[node].append(neighbor)
            adj_map[neighbor].append(node)


        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in adj_map[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n
