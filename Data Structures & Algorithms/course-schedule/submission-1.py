class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle detection
        # for each course, find the in degree, and courses it is a prerequisite for

        course_dependencies = defaultdict(list)
        course_indegree = {}
        for i in range(numCourses):
            course_indegree[i] = 0

        for target, prereq in prerequisites:
            course_indegree[target] += 1
            course_dependencies[prereq].append(target)
        
        res = 0
        queue = deque()
        for course, indegree in course_indegree.items():
            if indegree == 0:
                queue.append(course)
        while queue:
            res += 1
            course = queue.popleft()
            for dependent in course_dependencies[course]:
                course_indegree[dependent] -= 1
                if course_indegree[dependent] == 0:
                    queue.append(dependent)
        return res == numCourses