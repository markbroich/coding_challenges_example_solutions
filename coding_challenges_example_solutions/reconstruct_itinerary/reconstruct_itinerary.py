'''
Leetcode 332. 
Reconstruct Itinerary


You are given a list of airline tickets where tickets[i] = [fromi, toi]
represent the departure and the arrival airports of one flight. Reconstruct
the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary
must begin with "JFK". If there are multiple valid itineraries, you should
return the itinerary that has the smallest lexical order when read as a single
string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order
than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all
the tickets once and only once.


Example 1:
Input: tickets = [["MUC", "LHR"],["JFK", "MUC"],["SFO", "SJC"],["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg

Example 2:
Input: tickets = [["JFK", "SFO"],["JFK", "ATL"],["SFO", "ATL"],["ATL", "JFK"],
                  ["ATL", "SFO"]]
Output: ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
Explanation: Another possible reconstruction is
["JFK", "SFO", "ATL", "JFK", "ATL", "SFO"] but it is larger in lexical order.
https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg

Constraints:
1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
'''

# solution using recursive backtracking
# sorting ensures condition is meet but is greedy.


def solve(tickets):
    # Worth case is to backtrack all combiantions
    # So number of flights^maxDestiantions
    # So, O(f^maxD) where f is number of flights and maxD is max 
    # destiantions from an airport
    # the likely runtime is much less due to a solution beeing found w/o having to 
    # eval all combinations of flights from all airports
    def dfs(route, tickets, ori):
        route = route + [ori]
        if len(tickets) == 0:
            # if I am out of tickets, 
            # I got a solution
            return True, route
        destLst = [t for t in tickets if t[0] == ori]
        # sort dest so to try the lexiograpically smaller once first
        # O(v log(v)) where v is vertices
        # Os(1)
        destLst.sort()
        for ori, dest in destLst:
            tickets.remove([ori, dest])
            res, resRoute = dfs(route, tickets, dest)
            if res:
                return True, resRoute
            # backtrack
            tickets.append([ori, dest])
        # if I still have tickets but can not move, 
        # the path is invalid
        return False, route

    return dfs([], tickets, ori="JFK")[1]

# ex1
tickets = [["JFK", "SFO"],
           ["JFK", "ATL"],
           ["SFO", "ATL"],
           ["ATL", "JFK"],
           ["ATL", "SFO"]]
exp = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
print(solve(tickets) == exp)

# ex 2
tickets = [["MUC", "LHR"],["JFK", "MUC"],["SFO", "SJC"],["LHR", "SFO"]]
exp = ["JFK", "MUC", "LHR", "SFO", "SJC"]
print(solve(tickets) == exp)


# There is a faster solution using the
# eulerian path where the route is built from back to front
# by adding an airport to the end of the route, 
# once we have taken all outgoing flights. At that point we go back one airport
# and travel until we are at and aritport where we have taken all outgoing flights
# we add that airport to the fornt of the route and repeat.

# Ot(e log(e/v))
# Os(e + v)
def solve(tickets, o='JFK'):
    # Ot(e+v) where n is ticket count
    # Os(e+v)
    myGraph = pop_dict(tickets)
    # Ot(e log(e/v))
    myGraph = sort_dict_valueLst(myGraph)

    # Eulerian Path so visits each edge once:
    # so Ot(e) 
    # stack memory Os(e)
    def dfs(myDict, o):
        while myDict[o]:
            d = myDict[o][0]
            del myDict[o][0]
            if d in myDict:
                dfs(myDict, d)
            else:
                route.append(d)
        route.append(o)

    route = []
    dfs(myGraph, o)

    route = revLst(route)
    # to reverse also use:
    # route.reverse()
    # route = route[::-1]
    return route


# Ot(e+v) where n is ticket count
# Os(e+v)
def pop_dict(tickets):
    myDict = {}
    for o, d in tickets:
        if o in myDict:
            myDict[o].append(d)
        else:
            myDict[o] = [d]
    return myDict


# Ot(e log(e/v)). where e are the edges and v are the vertices
# Normal would be n log(n) 
# but we can assume equal distribution of edges per vertice so e/v per 
# edge outcoing and e/v returning so e/v*2. Simpligying to e log(e/v). 
# Os()
def sort_dict_valueLst(myDict):
    for k in myDict:
        myDict[k] = sorted(myDict[k])
    return myDict


# Ot(n) where n is length of lst
# Os(1)
def revLst(lst):
    for i in range(0, int(len(lst)/2)):
        lst[len(lst)-1-i], lst[i] = lst[i], lst[len(lst)-1-i] 
    return lst


# Run code
tickets = [["JFK", "SFO"],
           ["JFK", "ATL"],
           ["SFO", "ATL"],
           ["ATL", "JFK"],
           ["ATL", "SFO"]]
exp = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
print(solve(tickets) == exp)

tickets = [["MUC", "LHR"],["JFK", "MUC"],["SFO", "SJC"],["LHR", "SFO"]]
exp = ["JFK", "MUC", "LHR", "SFO", "SJC"]
print(solve(tickets) == exp)