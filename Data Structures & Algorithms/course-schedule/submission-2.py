class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create graph representation through hash map where key = course, val: prereq list
        prereq_map = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if prereq_map[course] == []:
                return True
            
            visit.add(course)
            for pre in prereq_map[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            prereq_map[course] = []
            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True
    


    # Time Complexity: O(V+E)
    # Space COmplexity: O(V+E)
        