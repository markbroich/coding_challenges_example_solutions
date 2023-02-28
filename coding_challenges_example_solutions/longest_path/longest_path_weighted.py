'''
Find the shortest and longest path through an weighted, directed graph

Exampel:
graph = {from_node: (to_node, distance)}

start = 1
end = 5
graph = {1:[(2,7),(3,9),(6,14)],
            2:[(4,15)],
            3:[(2,10),(4,15),(6,2)],
            4:[(5,6)],
            5:[],
            6:[(5,9)]
            }

shortest = 20
longest = 30
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


# inefficient! Using a heap would help
def find_next_smallest_node(dist_so_far, complete):
    value=float('inf')
    node = None
    for k, v in dist_so_far.items():
        if k not in complete:
            if v < value:
                value = v
                node = k
    return node


def dykstra_longest(graph, start, end):
    # init
    dist_so_far = {k: float('-inf') for k in graph}
    dist_so_far[start] = 0
    if start not in dist_so_far or end not in dist_so_far:
        return -1
    node = start

    complete = set()
    while node:
        complete.add(node)
        for k, d in graph[node]:
            if k not in complete:
                dist_so_far[k] = max(dist_so_far[k], dist_so_far[node] + d)
        node = find_next_largest_node(dist_so_far, complete, end)
        # print(node)
    return dist_so_far[end]


# inefficient! Using a heap would help
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
    # Directed graph
    start = 1
    end = 5
    graph3 = {1:[(2,7),(3,9),(6,14)],
              2:[(4,15)],
              3:[(2,10),(4,15),(6,2)],
              4:[(5,6)],
              5:[],
              6:[(5,9)]
              }

    shortest3 = 20
    longest3 = 30
    print('Directed graph:')
    print(dykstra_shortest(graph3, start, end) == shortest3)
    print(dykstra_longest(graph3, start, end) == longest3)


    # undirected graphs work for dykstra_shortest only.
    start = 1
    end = 4
    graph1 = {1:[(2,1)], 2:[(1,1),(3,1),(4,3)], 3:[(2,1),(4,1)], 4:[(3,1),(2,3)]}
    shortest1 = 3
    print(dykstra_shortest(graph1, start, end) == shortest1)

    graph2 = {1:[(2,1)], 2:[(1,1),(3,1)], 3:[(2,1)]}
    shortest2 = -1
    print(dykstra_shortest(graph2, start, end) == shortest2)

    graph1 = {1:[(2,1)], 2:[(1,1),(3,1),(4,3)], 3:[(2,1),(4,1)], 4:[(3,1),(2,3)]}
    shortest1 = 3
    print(dykstra_shortest(graph1, start, end) == shortest1)

    graph2 = {1:[(2,1)], 2:[(1,1),(3,1)], 3:[(2,1)]}
    shortest2 = -1
    print(dykstra_shortest(graph2, start, end) == shortest2)


tests()
