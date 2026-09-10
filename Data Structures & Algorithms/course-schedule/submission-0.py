class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Have a hashmap with each course and its prerequisites. Run dfs on each course, and if it's already in the visiting set, return false. If it has no prerequisites, return true. These are the base conditions. If neither of these two are satisfied, add it to the visiting set, run a dfs on its prerequisite courses, return false if not satisfying conditions, then remove it from the visiting set, set its prereqs to [] for easier computation and return true.
        # Complexities: O(V + E), O(V + E)
        preMap = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        visitSet = set()

        def dfs(course):
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True

            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visitSet.remove(course)

            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True