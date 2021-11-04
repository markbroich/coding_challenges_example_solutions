'''
Minimizing Permutations

In this problem, you are given an integer N, and a permutation, P of the
integers from 1 to N, denoted as (a_1, a_2, ..., a_N). 
You want to rearrange the elements of the permutation into increasing order,
repeatedly making the following operation:
Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its
order.
Your goal is to compute the minimum number of such operations required to
return the permutation to increasing order.

Signature
int minOperations(int[] arr)

Input
Array arr is a permutation of all integers from 1 to N, N is between 1 and 8

Output
An integer denoting the minimum number of operations required to arrange the
permutation in increasing order

Example
If N = 3, and P = (3, 1, 2), we can do the following operations:
Select (1, 2) and reverse it: P = (3, 2, 1).
Select (3, 2, 1) and reverse it: P = (1, 2, 3).
output = 2
'''


def minOperations(myTup):
    myTup = tuple(myTup)
    target = tuple([i for i in range(1, len(myTup) + 1)])
    # O(n*get_perm_indices) where n is all nodes in the graph and
    # get_perm_indices has a runtime of Ot(n! / (n − r)!) where
    # n is legth of arr, and r is number
    # to draw = 2 (order matters)
    # which makes this a factorial runtime
    #
    # populate graph
    G = pop_graph(myTup)
    # BFS to find shortest path
    return bfs_shoertest_path(target, myTup, G)


def pop_graph(myTup):
    # populate graph
    G = {}
    seen = set()
    # use a BFS to populate the graph
    queue = [myTup]
    while queue:
        curTup = queue.pop(0)
        if curTup not in seen:
            seen.add((curTup))
            # get start end indices of possible permutations of curTup
            # returns a Lst of tup
            permLst = get_perm_indices(curTup)
            # create the swaps as per permLst
            # returns a Lst of swap results
            edgeLst = create_edges(curTup, permLst)
            G[curTup] = edgeLst
            queue = queue + edgeLst
    return G


# Ot(n! / (n − r)!) where n is legth of arr, and r is number
# to draw = 2 (order matters)
# Os(n! / (n - r)!)
def get_perm_indices(curTup):
    # get start end indices of possible permutations of curTup
    # returns a Lst of tup
    idxLst = [i for i in range(0, len(curTup))]
    permLst = []

    def rec(pre, post):
        if pre and len(pre) == 2:
            permLst.append((pre[0], pre[1]))
            return
        if not pre:
            for i in range(0, len(post)):
                rec(pre + [post[i]], post[:i] + post[i+1:])
        else:
            for i in range(pre[0], len(post)):
                rec(pre + [post[i]], post[:i] + post[i+1:])
    rec([], idxLst)
    return permLst


def create_edges(curTup, permLst):
    # create the swaps as per permLst
    # returns a Lst of swap results
    edgeLst = []
    for s, e in permLst:
        arr = list(curTup)
        temp = arr[s:e+1]
        temp = temp[::-1]
        arr[s:e+1] = temp
        edgeLst.append(tuple(arr))
    return edgeLst


def bfs_shoertest_path(target, myTup, G):
    # does BFS to find and returns shortest pass
    # from input (myTup tp target)
    queue = [(0, myTup)]
    seen = set()
    while queue:
        d, curTup = queue.pop(0)
        if curTup == target:
            return d
        if curTup not in seen:
            seen.add(curTup)
            for n in G[curTup]:
                queue.append((d + 1, n))
    return -1


N = 3
P = (3, 1, 2)
print(minOperations(P) == 2)

N = 5
P = (4, 1, 2, 5, 3)
print(minOperations(P) == 3)

N = 5
P = (1, 2, 5, 4, 3)
print(minOperations(P) == 1)

N = 3
P = (3, 1, 2)
print(minOperations(P) == 2)

N = 7
P = (2, 1, 3, 4, 6, 5, 7)
print(minOperations(P) == 2)
