# 4 jug problem with constant total volume of liquid

# Three men robbed a gentleman of a vase, containing 24 ounces of balsam. 
# Whilst running away they met a glass seller, 
# of whom they purchased three vessels. 
# On reaching a place of safety they wished to divide the booty, 
# but found that their vessels could hold 5, 11, and 13 ounces, 
# respectively. 
#
# How could they divide the balsam into equal portions?

# the approach is to create a directed graph recording all states 
# as nodes and all transactions as edges to the find the shortest 
# path from the start state to the desired state

# so the scenario is: 
# startContent = (0, 0, 0, 24)
# capacities = (5, 11, 13, 24)
# endContent = (0, 8, 8, 8)


def build_gallon_graph(g, content, capacities, stopAt):
    # stop once value given by stopAt has been created
    if stopAt in g:
        return g
    #
    num_jugs = len(content)
    # number of permutations of pouring from one vessel to another is: 
    # factorial(num_jugs) / factorial(num_jugs -2)
    for from_ in range(num_jugs):
        for to_ in range(num_jugs):
            if from_ != to_:
                for newContent in transitions(content, capacities, from_, to_):
                    newContent = tuple(newContent)
                    g = _add_connection(g, content, newContent,
                        capacities, stopAt) 
    return g

def transitions(content, capacities, from_, to_):
    transfer = min(content[from_], capacities[to_] - content[to_])
    if transfer > 0:
        content = list(content[:])        # Copy the current state (content)
        content[from_] -= transfer
        content[to_] += transfer
        yield tuple(content)              # Return the new state (content)

def _add_connection(g, content, newContent, capacities, stopAt):
    if not newContent in g:
        # add node
        g[newContent] = []
    if not _connection_exists(g, content, newContent):
        g[content].append(newContent)
        g = build_gallon_graph(g, newContent, capacities, stopAt)
    return g

def _connection_exists(g, content, newContent):
    if newContent in g[content]:
        return True
    return False

def _bfs(g, start, end, queue, dist, previous):
    if start == end:
        return dist, previous
    #
    start = queue.pop(0)
    for node in g[start]:
        if node not in dist:      
            queue.append(node)
            dist[node] = dist[start] + 1
            previous[node] = start
    dist, previous = _bfs(g, start, end, queue, dist, previous)
    return dist, previous

def _list_shortest_path_steps(previous, start, end):
    # init list of shortest_path_steps with the end node 
    path = [end]
    # backtrace the previous dict until start has been reached
    # and append nodes to front of list
    while previous[end] != start:
        end = previous[end]
        path.insert(0,end)
    # insert tart node at front of list and return
    path.insert(0,start)
    return(path)


##########################################
# run the code
startContent = (0, 0, 0, 24)
capacities = (5, 11, 13, 24)
endContent = (0, 8, 8, 8)

# make graph node w start state 
g={startContent:[]}

# build the graph
# if stopAt= endContent, the graph building will stop when 
# the endContent state has been generated. 
g = build_gallon_graph(g, startContent, capacities, stopAt=endContent)

# find shortest path
queue = [(startContent)]
dist = {startContent: 0}
previous = {startContent: None}
dist, previous = _bfs(g, startContent, endContent, queue, dist, previous)
shortestPathSteps = _list_shortest_path_steps(previous, startContent, endContent)
print('the min steps from the start state to the end state are: ')
print(shortestPathSteps)


# problem featuring 4 jugs with fixed amount of liquid from: http://cut-the-knot.org/ctk/Water.shtml
# with inspiration from: https://codereview.stackexchange.com/questions/78586/pouring-water-between-two-jugs-to-get-a-certain-amount-in-one-of-the-jugs
# with inspiration from: https://codereview.stackexchange.com/questions/219033/jug-problem-3-jugs