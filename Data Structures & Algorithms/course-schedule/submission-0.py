class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prerequisite_map = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prerequisite_map[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prerequisite_map[course] == []:
                return True

            visited.add(course)
            for pre in prerequisite_map[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            prerequisite_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
