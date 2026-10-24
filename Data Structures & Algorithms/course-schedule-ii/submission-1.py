class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_dependencies = defaultdict(list)
        course_indegree = {}
        for i in range(numCourses):
            course_indegree[i] = 0

        for target, prereq in prerequisites:
            course_indegree[target] += 1
            course_dependencies[prereq].append(target)
        
        res = []
        queue = deque()
        for course, indegree in course_indegree.items():
            if indegree == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            res.append(course)
            for dependent in course_dependencies[course]:
                course_indegree[dependent] -= 1
                if course_indegree[dependent] == 0:
                    queue.append(dependent)
        return res if len(res) == numCourses else []