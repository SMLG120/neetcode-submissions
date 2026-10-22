class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visitSet = set()
        def dfs(crs):
            # if found crs in visitSet -> cycle detected
            if crs in visitSet:
                return False
            # reach base case return True
            if preMap[crs] == []:
                return True
            # add course to set
            visitSet.add(crs)
            # visit the prerequisites to see if they also have prerequisites
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visitSet.remove(crs)
            # courses that passed all previous tests don't have prerequisites, so set to []
            preMap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
