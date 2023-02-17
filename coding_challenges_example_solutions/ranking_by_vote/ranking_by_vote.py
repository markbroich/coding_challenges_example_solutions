# Ranking by votes
# https://leetcode.com/problems/rank-teams-by-votes/

'''
In a special ranking system, each voter gives a rank from highest to lowest to all teams
participating in the competition.

The ordering of teams is decided by who received the most position-one votes.
If two or more teams tie in the first position, we consider the second position
to resolve the conflict, if they tie again, we continue this process until the
ties are resolved. If two or more teams are still tied after considering all positions,
we rank them alphabetically based on their team letter.

You are given an array of strings votes which is the votes of all voters in the ranking systems.
Sort all teams according to the ranking system described above.


Return a string of all teams sorted by the ranking system.

Example 1
Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: 
  Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
  Team B was ranked second by 2 voters and ranked third by 3 voters.
  Team C was ranked second by 3 voters and ranked third by 2 voters.
  As most of the voters ranked C second, team C is the second team, and team B is the third.

Example 2
Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation:
  X is the winner due to the tie-breaking rule. X has the same votes as W for the first position, 
  but X has one vote in the second position, while W does not have any votes in the second position.

Example 3
Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter, so their votes are used for the ranking.
'''

import functools


# Ot(v * w + k * m * log(m)), Os(m * m)
# where v is number of voters and w is
# number of votes. m is number of teams
# and k is up to the number of sorting criteria.
# In some cases k may be small if a tie can be broken early.
# k may be as large as m.
def rank_by_votes(votes):
    # Ot(v * w) Os(m * m)
    rank_count_dict = pop_dict(votes)

    # Ot(kmlogm), Os(m)
    # m is number of teams and k is up to the number of sorting criteria.
    # In some cases k may be small if a tie can be broken early
    def comp(a, b):
        for r in rank_count_dict[a]:
            if (rank_count_dict[a][r] < rank_count_dict[b][r]):
                return 1
            elif (rank_count_dict[a][r] > rank_count_dict[b][r]):
                return -1
        if a > b:
            return 1
        return -1
    res = sorted(rank_count_dict, key=functools.cmp_to_key(comp))

    # O(m)
    return ''.join(res)


# Ot(v*w) where v is number of voters and w is
# number of votes.
# Os(m*r) where m is number of teams
# (m == r where r is number of indev rankes)
def pop_dict(votes):
    teamset = set()
    rank_count_dict = {}    
    for v in votes:
        for t in v:
            teamset.add(t)
    ranks = len(teamset)
    for v in votes:
        for i, t in enumerate(v):
            if t not in rank_count_dict:
                rank_count_dict[t] = {r: 0 for r in range(ranks)}
                rank_count_dict[t][i] = 1
            else:
                rank_count_dict[t][i] += 1
    return rank_count_dict


def tests():
    votes = ["ABC","ACB","ABC","ACB","ACB"]
    expected = "ACB"
    # Explanation: 
    #   Team A was ranked first place by 5 voters. No other team was voted
    #   as first place, so team A is the first team.
    #   Team B was ranked second by 2 voters and ranked third by 3 voters.
    #   Team C was ranked second by 3 voters and ranked third by 2 voters.
    #   As most of the voters ranked C second, team C is the second team,
    #   and team B is the third.
    print(rank_by_votes(votes) == expected)

    votes = ["BAC", "ABC"]
    expected = "ABC"
    print(rank_by_votes(votes) == expected)

    votes = ["WXYZ","XYZW"]
    expected = "XWYZ"
    # Explanation:
    # 	X is the winner due to the tie-breaking rule. X has the same votes
    #   as W for the first position,
    #   but X has one vote in the second position, while W does not have
    #   any votes in the second position.
    print(rank_by_votes(votes) == expected)

    votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
    expected = "ZMNAGUEDSJYLBOPHRQICWFXTVK"
    print(rank_by_votes(votes) == expected)

    votes = ["WXYA","XYZA","YAWX"]
    expected = "YXWAZ"
    print(rank_by_votes(votes) == expected)


tests()
