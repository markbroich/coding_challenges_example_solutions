"""
Course Schedule

There are a total of numCourses courses you have to take, labeled from 0
to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to
first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: True
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: False
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you
should also have finished course 1. So it is impossible.

Example 3:
numCourses = 7
Output: True
prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from collections import defaultdict
from typing import List


# O(n + p) we need to visit every node and traverse on each
# prerequisite edge
def can_finish(n: int, prerequisites: list) -> bool:
    # O(n)
    free_courses = set()
    [free_courses.add(i) for i in range(n)]

    graph_prerequ_count = {}
    graph_is_pre_of = {}
    # Ot(p) Os(2p) where p is length of
    # prerequisites
    for course, pre in prerequisites:
        if course in free_courses:
            free_courses.remove(course)
        if course not in graph_prerequ_count:
            graph_prerequ_count[course] = 1
        else:
            graph_prerequ_count[course] += 1
        #
        if pre not in graph_is_pre_of:
            graph_is_pre_of[pre] = [course]
        else:
            graph_is_pre_of[pre].append(course)

    # dfs
    # O(n + p) we need to visit every node and traverse on each
    # prerequisite edge
    free_courses = list(free_courses)
    counter = len(free_courses)
    while free_courses:
        pre = free_courses.pop(0)
        if pre in graph_is_pre_of:
            for course in graph_is_pre_of[pre]:
                graph_prerequ_count[course] -= 1
                if graph_prerequ_count[course] == 0:
                    free_courses.append(course)
                    counter += 1
            del graph_is_pre_of[pre]

    if counter == n:
        return True
    return False


prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
numCourses = 7
expected = True
print(can_finish(numCourses, prerequisites) == expected)

prerequisites = [[1,0]]
numCourses = 2
expected = True
print(can_finish(numCourses, prerequisites) == expected)

prerequisites = [[1,0],[0,1]]
numCourses = 2
expected = False
print(can_finish(numCourses, prerequisites) == expected)

prerequisites = [[1, 0], [2, 0], [3, 2], [3, 1]]
n = 4
expected = True
print(can_finish(n, prerequisites) == expected)

prerequisites = [[1, 0], [2, 0], [3, 2], [3, 1], [0, 3]]
n = 4
expected = False
print(can_finish(n, prerequisites) == expected)

prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
n = 5
expected = True
print(can_finish(n, prerequisites) == expected)
print()


##
def can_finish(numCourses, prerequisites):
    all_courses = defaultdict(set)
    all_pre_courses = defaultdict(set)
    no_pre_courses = set()

    for courses, pre_courses in prerequisites:
        all_courses[courses].add(pre_courses)
        all_pre_courses[pre_courses].add(courses)
        no_pre_courses.add(courses)
        no_pre_courses.add(pre_courses)

    for course, pre_course in all_courses.items():
        if pre_course:
            no_pre_courses.remove(course)

    counter = 0
    # start with the no_prerequesit_courses
    stack = list(no_pre_courses)
    while stack:
        current = stack.pop()
        # count a course as taken
        counter += 1
        # for the courses that have the current prerequisites,
        # mark it as taken by removing it.
        # If no prerequisite left for a course, append it to the stack.
        for course in all_pre_courses[current]:
            all_courses[course].remove(current)
            if not all_courses[course]:
                stack.append(course)

    # stack will be empty with a counter < numCourses if
    # there is not all prerequisites can be takes
    # (if there is a circle in the graph)
    return counter == numCourses


prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
numCourses = 7
expected = True
print(can_finish(numCourses, prerequisites) == expected)

prerequisites = [[1,0]]
numCourses = 2
expected = True
print(can_finish(numCourses, prerequisites) == expected)

prerequisites = [[1,0],[0,1]]
numCourses = 2
expected = False
print(can_finish(numCourses, prerequisites) == expected)

prerequisites = [[1, 0], [2, 0], [3, 2], [3, 1]]
n = 4
expected = True
print(can_finish(n, prerequisites) == expected)

prerequisites = [[1, 0], [2, 0], [3, 2], [3, 1], [0, 3]]
n = 4
expected = False
print(can_finish(n, prerequisites) == expected)

prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
n = 5
expected = True
print(can_finish(n, prerequisites) == expected)
print()


# The most elegant algorithm
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for first, second in prerequisites:
            graph[first].append(second)
        # 0 = unknown # 1 = visiting # 2 = visited
        visit = [0] * numCourses

        def dfs(curr, visit):
            if visit[curr] == 1:
                return True
            if visit[curr] == 2:
                return False
            visit[curr] = 1
            for j in graph[curr]:
                if dfs(j, visit):
                    return True
            visit[curr] = 2
            return False

        for i in range(numCourses):
            if dfs(i, visit):
                return False

        return True


S1 = Solution()
prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
n = 7
expected = True
print(S1.canFinish(n, prerequisites) == True)


# Input: numCourses = 2, 
prerequisites = [[1,0]]
# Output: true
n = 2
expected = True
print(S1.canFinish(n, prerequisites) == expected)

# Input: numCourses = 2, 
prerequisites = [[1,0],[0,1]]
expected = False
n = 2
print(S1.canFinish(n, prerequisites) == expected)


prerequisites = [[1, 0], [2, 0], [3, 2], [3, 1]]
n = 4
expected = True
print(S1.canFinish(n, prerequisites) == expected)

prerequisites = [[1, 0], [2, 0], [3, 2], [3, 1], [0, 3]]
n = 4
expected = False
print(S1.canFinish(n, prerequisites) == expected)

prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
n = 5
expected = True
print(S1.canFinish(n, prerequisites) == expected)
print()


# https://leetcode.com/problems/course-schedule-ii/
# Here I return the order of the courses.
# If a cycle exists, I return None
def course_order(n, prerequisites):
    free_courses = set()
    [free_courses.add(i) for i in range(n)]

    graph_prerequ_count = {}
    graph_is_pre_of = {}
    # Ot(p) Os(2p) where p is length of
    # prerequisites
    for course, pre in prerequisites:
        if course in free_courses:
            free_courses.remove(course)
        if course not in graph_prerequ_count:
            graph_prerequ_count[course] = 1
        else:
            graph_prerequ_count[course] += 1
        #
        if pre not in graph_is_pre_of:
            graph_is_pre_of[pre] = [course]
        else:
            graph_is_pre_of[pre].append(course)

    # dfs
    # O(n + p) we need to visit every node and traverse on each
    # prerequisite edge
    order_of_courses = []
    free_courses = [list(free_courses)]
    counter = len(free_courses[0])
    while free_courses:
        pre_batch = free_courses.pop(0)
        order_of_courses.append(pre_batch)
        for pre in pre_batch:
            new_pre_batch = []
            if pre in graph_is_pre_of:
                for course in graph_is_pre_of[pre]:
                    graph_prerequ_count[course] -= 1
                    if graph_prerequ_count[course] == 0:
                        new_pre_batch.append(course)
                        counter += 1
                del graph_is_pre_of[pre]
            if new_pre_batch:
                free_courses.append(new_pre_batch)

    if counter == n:
        return order_of_courses
    return None


prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
numCourses = 7
expected = [[6], [5], [4], [2], [3], [0], [1]]
print(course_order(numCourses, prerequisites) == expected)

prerequisites = [[1,0]]
numCourses = 2
expected = [[0], [1]]
print(course_order(numCourses, prerequisites) == expected)

prerequisites = [[1,0],[0,1]]
numCourses = 2
expected = None
print(course_order(numCourses, prerequisites) == expected)

prerequisites = [[1, 0], [2, 0], [3, 2], [3, 1]]
numCourses = 4
expected = [[0], [1, 2], [3]]
print(course_order(numCourses, prerequisites) == expected)

prerequisites = [[1, 0], [2, 0], [3, 2], [3, 1], [0, 3]]
numCourses = 4
expected = None
print(course_order(n, prerequisites) == expected)

prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
numCourses = 5
expected = [[2, 4], [3], [1], [0]]
print(course_order(numCourses, prerequisites) == expected)
