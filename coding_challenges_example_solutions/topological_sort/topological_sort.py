'''Topological sorting for Directed Acyclic Graph (DAG) is a
linear ordering of vertices such that for every directed edge u v,
vertex u comes before v in the ordering.

There may be multiple possible orderings.

Note: Topological Sorting for a graph is not possible
if the graph is not a DAG.

graph = {
    5: 2,
    5: 0,
    4: 0,
    4: 1,
    2: 3,
    3: 1}
expected = [5, 4, 2, 3, 1, 0]

graph = {
    5: 2,
    5: 0,
    4: 0,
    4: 1,
    2: 3,
    3: 1,
    2: 0}
# has a circle
expected = []
'''


def topo_sort(graph: dict) -> list:
    result = []
    status = {}

    def rec(node):
        if node in status and status[node] == 'done':
            return True
        elif node in status and status[node] == 'in_process':
            return False
        status[node] = 'in_process'
        if node in graph:
            for child in graph[node]:
                if not rec(child):
                    return False
        status[node] = 'done'
        result.append(node)
        return True

    for k in graph.keys():
        if not rec(k):
            return []
    return result[::-1]



graph = {
    5: [0, 2],
    4: [0],
    4: [1],
    2: [3],
    3: [1]
    }

expected = [4, 5, 2, 3, 1, 0]
print(topo_sort(graph) == expected)

graph = {
    5: [0, 2],
    4: [0],
    4: [1],
    2: [3],
    3: [1, 5]}

expected = []
print(topo_sort(graph) == expected)


graph = {
    5: [11],
    7: [11, 8],
    3: [8, 10],
    11: [2, 9, 10],
    8: [9]
    }
expected = [3, 7, 8, 5, 11, 10, 9, 2]
print(topo_sort(graph) == expected)