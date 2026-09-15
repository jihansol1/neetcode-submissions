class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # create adj_map of nodes and its neighbors
        # need to connect both node -> parent and parent -> node since graph is undirected
        # to be a tree needs all nodes connected + no cycles

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