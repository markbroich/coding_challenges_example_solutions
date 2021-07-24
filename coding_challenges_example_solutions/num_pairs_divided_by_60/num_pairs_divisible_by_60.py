"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. 
Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
numPairsDivisibleBy60
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

(a + b) % 60 == 0
(a % 60 + b % 60) % 60 == 0 => a % 60 = 0 and b % 60 = 0 OR a % 60 + b % 60 = 60
b % 60 = 60 - a % 60 


So, check if either a % 60 == 0 and b % 60 == 0 OR
a % 60 != 0 and 60 - b % 60 == a % 60 
"""


def numPairsDivisibleBy60(time, secs=60):
    myDict = {}
    paircnt = 0
    for i in range(0,len(time)):
        if 0 in myDict and time[i] % secs == 0:
            paircnt += myDict[0]
        elif secs - time[i] % secs in myDict:
            paircnt += myDict[secs - time[i] % secs]
        # add to MyDict
        if time[i] % secs in myDict:
            myDict[time[i] % secs] += 1
        else:
            myDict[time[i] % secs] = 1
    return paircnt


# using collections
import collections

def numPairsDivisibleBy60_colections(time):
    remainders = collections.defaultdict(int)
    ret = 0
    for t in time:
        if t % 60 == 0: # check if a%60==0 && b%60==0
            ret += remainders[0]
        else: # check if a%60+b%60==60
            ret += remainders[60-t%60]
        remainders[t % 60] += 1 # remember to update the remainders
    return ret


time = [30,20,150,100,40]
print(numPairsDivisibleBy60(time) == 3)
print(numPairsDivisibleBy60_colections(time) == 3)
time = [60,60,60]
print(numPairsDivisibleBy60(time) == 3)
print(numPairsDivisibleBy60_colections(time) == 3)
time = [20,40]
print(numPairsDivisibleBy60(time) == 1)
print(numPairsDivisibleBy60_colections(time) == 1)




