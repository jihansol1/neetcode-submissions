class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # creating the hash map to represent graph with courses and its prereq list
        prereq_map = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        # visited: completely finsihed this course?
        # cycle: currently exploring this course?
        visited, cycle = set(), set()
        ans = []

        def dfs(course):
            if course in visited:
                return True
            if course in cycle: 
                return False

            cycle.add(course)

            for pre in prereq_map[course]:
                if dfs(pre) == False:
                    return False

            cycle.remove(course)
            visited.add(course)
            ans.append(course)
            return True


        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return ans 

        