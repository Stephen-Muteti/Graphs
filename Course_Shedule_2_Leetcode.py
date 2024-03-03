"""
There are a total of numCourses courses you have to take, 
labeled from 0 to numCourses - 1. You are given an array prerequisites 
where prerequisites[i] = [ai, bi] indicates that you must take course bi 
first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.
"""


def findOrder(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    def prepareGraph(n,pre):
        graph = {}
        indegree = [0]*n
        for pr in pre:
            if not pr[1] in graph: graph[pr[1]] = []
            graph[pr[1]].append(pr[0])
            indegree[pr[0]] += 1
        return graph,indegree
    
    graph,indegree = prepareGraph(numCourses,prerequisites)
    
    #BFS
    courses = []
    q = deque()
    for vtx in range(numCourses):
        if indegree[vtx] == 0: q.append(vtx)
    
    while q:
        cur_course = q.popleft()
        courses.append(cur_course)

        if cur_course in graph:
            for neighbour in graph[cur_course]:

                indegree[neighbour] -= 1
                if indegree[neighbour] == 0: q.append(neighbour)        
    
    return courses if len(courses) == numCourses else []