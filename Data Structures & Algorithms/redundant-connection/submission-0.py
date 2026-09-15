class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # because there are n nodes and n edges, there will be 1 cycle in the graph
        n = len(edges)
        # create an empty adjcacency map that will be connected as we go -> if cycle detected return the last edge added
        adj_map = {i:[] for i in range(1, n+1)}

        # node = curr node, target = node/neighbor trying to reach from curr node, visited = visited nodes set
        def dfs(node, target, visited):
            # if node == target, we have a cycle
            if node == target:
                return True
                
            visited.add(node)

            for neighbor in adj_map[node]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False

        for node, neighbor in edges:
            if dfs(node, neighbor, set()):
                return [node, neighbor]

            adj_map[node].append(neighbor)
            adj_map[neighbor].append(node)



         