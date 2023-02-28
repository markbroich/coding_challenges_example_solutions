'''
Find the shortest and longest path through an weighted graph

Exampel 1
from_node: (to_node, distance)
start = 1
end = 4
graph1 = {1:[(2,1)], 2:[(1,1),(3,1),(4,3)], 3:[(2,1),(4,1)], 4:[(3,1),(2,3)]}
shotrest1 = 3
'''


def dykstra_shortest(graph, start, end):
    # init
    min_so_far = {k: float('inf') for k in graph}
    min_so_far[start] = 0
    if start not in min_so_far or end not in min_so_far:
        return -1
    node = start

    complete = set()
    while node:
        complete.add(node)
        for k, d in graph[node]:
            if k not in complete:
                min_so_far[k] = min(min_so_far[k], min_so_far[node] + d)
        node = find_next_smallest_node(min_so_far, complete)
    return min_so_far[end]


# inefficient!
def find_next_smallest_node(dist_so_far, complete):
    value=float('inf')
    node = None
    for k, v in dist_so_far.items():
        if k not in complete:
            if v < value:
                value = v
                node = k
    return node


def find_next_largest_node(dist_so_far, complete, end):
    value=float('-inf')
    node = None
    for k, v in dist_so_far.items():
        if k not in complete and k != end:
            if v > value:
                value = v
                node = k
    return node


def tests():
    start = 1
    end = 4
    graph1 = {1:[(2,1)], 2:[(1,1),(3,1),(4,3)], 3:[(2,1),(4,1)], 4:[(3,1),(2,3)]}
    shotrest1 = 3
    print(dykstra_shortest(graph1, start, end) == shotrest1)

    start = 1
    end = 4
    graph2 = {1:[(2,1)], 2:[(1,1),(3,1)], 3:[(2,1)]}
    shotrest2 = -1
    print(dykstra_shortest(graph2, start, end) == shotrest2)

    #
    start = 1
    end = 4
    graph1 = {1:[(2,1)], 2:[(1,1),(3,1),(4,3)], 3:[(2,1),(4,1)], 4:[(3,1),(2,3)]}
    shotrest1 = 3
    print(dykstra_shortest(graph1, start, end) == shotrest1)

    start = 1
    end = 4
    graph2 = {1:[(2,1)], 2:[(1,1),(3,1)], 3:[(2,1)]}
    shotrest2 = -1
    print(dykstra_shortest(graph2, start, end) == shotrest2)


    # longest: TBD

tests()
