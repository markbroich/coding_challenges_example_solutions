'''
Find the shortest and longest path through an unweighted graph

Exampel 1
graph1 = {1:[2], 2:[1,3,4], 3:[2,4], 4:[2,3]}
steps_shortest1 = 2
steps_shortest1 = 3

Exampel 2
graph2 = {1:[2,3,9], 2:[1,3,5], 3:[1,2,4], 4:[3,5,6,7], 5:[2,4,6,9],
        6:[4,5,7], 7:[4,6], 9:[1,5]}
steps_shortest2 = 3
steps_longest2 = 7

Exampel 3
graph3 = {1:[2], 2:[1,3,4], 3:[2,4]}
steps_shortest3 = -1
steps_longest3 = -1
'''


# BFS
def shortest_path(graph, start, dest):
    queue = [(start, 0)]
    seen = set([start])
    while queue:
        cur, steps = queue.pop(0)
        if cur == dest:
            return steps
        seen.add(cur)
        for i in graph[cur]:
            if i not in seen:
                queue.append((i, steps + 1))
    return -1


# DFS
def shortest_path_dfs(graph, start, dest):
    def rec(i, steps, seen):
        if i == dest:
            return steps
        mini = float('inf')
        for j in graph[i]:
            if j not in seen:
                steps += 1
                seen.add(j)
                mini = min(rec(j, steps, seen), mini)
                seen.remove(j)
                steps -= 1
        return mini
    res = rec(start, 0, set([1]))
    if res == float('inf'):
        return -1
    return res


# DFS w modified rule (switching min to max)
def longest_path(graph, start, dest):
    def rec(i, steps, seen):
        if i == dest:
            return steps
        maxi = float('-inf')
        for j in graph[i]:
            if j not in seen:
                steps += 1
                seen.add(j)
                maxi = max(rec(j, steps, seen), maxi)
                seen.remove(j)
                steps -= 1
        return maxi
    res = rec(start, 0, set([1]))
    if res == float('-inf'):
        return -1
    return res


def tests():
    graph1 = {1:[2], 2:[1,3,4], 3:[2,4], 4:[2,3]}
    steps_shortest1 = 2
    steps_longest1 = 3

    graph2 = {1:[2,3,9], 2:[1,3,5], 3:[1,2,4], 4:[3,5,6,7], 5:[2,4,6,9],
            6:[4,5,7], 7:[4,6], 9:[1,5]} 
    steps_shortest2 = 3
    steps_longest2 = 7

    graph3 = {1:[2], 2:[1,3], 3:[2]}
    steps_shortest3 = -1
    steps_longest3 = -1

    print('1s)', shortest_path(graph1, 1, 4) == steps_shortest1)
    print('2s)', shortest_path(graph2, 1, 7) == steps_shortest2)
    print('3s)', shortest_path(graph3, 1, 4) == steps_shortest3)

    print('1s)', shortest_path_dfs(graph1, 1, 4) == steps_shortest1)
    print('2s)', shortest_path_dfs(graph2, 1, 7) == steps_shortest2)
    print('3s)', shortest_path_dfs(graph3, 1, 4) == steps_shortest3)

    print('3l)', longest_path(graph1, 1, 4) == steps_longest1)
    print('3l)', longest_path(graph2, 1, 7) == steps_longest2)
    print('3s)', longest_path(graph3, 1, 4) == steps_longest3)


tests()