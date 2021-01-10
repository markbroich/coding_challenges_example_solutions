# 2 jug problem
#
# we got two empty jugs with known capacity: 
# 5l and 3l
# the task is to find a way to measure 4l
# we can fill the jugs with an infint supply of water
# empty the jugs and pour water from one jug to the other. 

# the approach is to create a directed graph recording all states 
# as nodes and all transactions as edges to the find the shortest 
# path from the start state to the desired state

# so the scenario is: 
# startContent = (0,0)
# jug1_size, jug2_size = 5, 3
# endContent = (4,0)


def build_gallon_graph(g, jug1, jug2, jug1_size, jug2_size, stopAt=''):
    # stop once value given by stopAt has been created
    if stopAt in g:
        return g
    for new_jug1, new_jug2 in transitions(jug1, jug2, jug1_size, jug2_size):
        g = _add_connection(g, jug1, jug2, new_jug1, new_jug2,
                        jug1_size, jug2_size, stopAt=stopAt) 
    return g

def transitions(jug1, jug2, jug1_size, jug2_size):
    # Fill jug 1.
    if jug1 < jug1_size:
        yield jug1_size, jug2
    # Fill jug 2.
    if jug2 < jug2_size:
        yield jug1, jug2_size
    # Pour jug 1 to jug 2.
    measure = min(jug1, jug2_size - jug2)
    if measure > 0:
        yield jug1 - measure, jug2 + measure
    # Pour jug 2 to jug 1.
    measure = min(jug1_size - jug1, jug2)
    if measure > 0:
        yield jug1 + measure, jug2 - measure
    # Empty jug 1.
    if jug1 > 0:
        yield 0, jug2
    # Empty jug 2.
    if jug2 > 0:
        yield jug1, 0

def _add_connection(g, jug1, jug2, new_jug1, new_jug2, jug1_size, jug2_size, stopAt=''):
    if not (new_jug1, new_jug2) in g:
        # add node
        g[(new_jug1, new_jug2)] = []
    if not _connection_exists(g, jug1, jug2, new_jug1, new_jug2):
        g[(jug1, jug2)].append((new_jug1, new_jug2))
        g = build_gallon_graph(g, new_jug1, new_jug2, jug1_size, jug2_size, stopAt=stopAt)
    return g

def _connection_exists(g, jug1, jug2, new_jug1, new_jug2):
    if (new_jug1, new_jug2) in g[(jug1, jug2)]:
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
startContent = (0,0)
jug1_size, jug2_size = 5, 3
endContent = (4,0)

# make graph node w start state 
g={(startContent[0], startContent[1]):[]}

# build the graph
# if stopAt= endContent, the graph building will stop when 
# the endContent state has been generated. if stopAt='', 
# the entire state and transition space will be graphed
g = build_gallon_graph(g, startContent[0], startContent[1], jug1_size, jug2_size, stopAt=endContent)

# find shortest path
queue = [(startContent)]
dist = {startContent: 0}
previous = {startContent: None}
dist, previous = _bfs(g, startContent, endContent, queue, dist, previous)
shortestPathSteps = _list_shortest_path_steps(previous, startContent, endContent)
print('the min steps from the start state to the end state are: ')
print(shortestPathSteps)


# for large graphs and different endContent value queries, we can build the entire graph 
# rather than stop when stopAt combination has been created

# with inspiration from: https://codereview.stackexchange.com/questions/78586/pouring-water-between-two-jugs-to-get-a-certain-amount-in-one-of-the-jugs



