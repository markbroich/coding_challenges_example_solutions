'''
Revenue Milestones
We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones. Given an array of the revenue on each day, and an array of milestones Facebook wants to reach, return an array containing the days on which Facebook reached every milestone.
Signature
int[] getMilestoneDays(int[] revenues, int[] milestones)
Input
revenues is a length-N array representing how much revenue FB made on each day (from day 1 to day N). milestones is a length-K array of total revenue milestones.
Output
Return a length-K array where K_i is the day on which FB first had milestones[i] total revenue. If the milestone is never met, return -1.
Example
revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]
Explanation
On days 4, 5, and 6, FB has total revenue of $100, $150, and $210 respectively. Day 6 is the first time that FB has >= $200 of total revenue
'''


# Add any helper functions you may need here


def getMilestoneDays(revenues, milestones):
    # get indixes of milestons sorted on value
    # Ot(m * log(m)) were m are the number of milestones
    # Os(m)
    milestoneIx = sorted(range(0, len(milestones)), 
                         key=lambda i: milestones[i])
    i = 0
    res = [''] * len(milestones)
    mySum = revenues[i]
    # Ot(n) where n is the revenue steps (assuming that n is >> m).
    # Os(1)
    for j in milestoneIx:
        ms = milestones[j]
        while True:
            if mySum >= ms:
                res[j] = i + 1
                break
            i += 1
            if i >= len(revenues):
                break
            mySum += revenues[i]
    return res


# Ex 1
revenues = [100, 200, 300, 400, 500]
milestones = [300, 800, 1000, 1400]
expected = [2, 4, 4, 5]
print(getMilestoneDays(revenues, milestones) == expected)

# Ex 2
revenues = [700, 800, 600, 400, 600, 700]
milestones = [3100, 2200, 800, 2100, 1000]
expected = [5, 4, 2, 3, 2]
print(getMilestoneDays(revenues, milestones) == expected)

# Ex 3
revenues = [1, 1, 1, 1, 1]
milestones = [1, 2, 3, 4, 9]
expected = [1, 2, 3, 4, '']
print(getMilestoneDays(revenues, milestones) == expected)
