'''
Task Scheduler

Given a characters array tasks, representing the tasks a CPU needs to do,
where each letter represents a different task. Tasks could be done in any
order. Each task is done in one unit of time. For each unit of time, the
CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period
between two same tasks (the same letter in the array), that is that there must
be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take
to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle ->
idle -> A

Constraints:
1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
'''

from collections import Counter


class Solution_Equasion:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        # AAAABBBBCCDE，n=3
        # group multiple kinds of tasks into one group
        # ABXX | ABXX | ABXX | AB
        # X = elm other than A/B or idle period, elm other than the most
        # frequent can be viewed as idle
        # A/B dist 3
        c = Counter(tasks)
        # print(c)
        max_freq = c.most_common()[0][1]
        max_nmbr = len([(elm, freq) for elm, freq in c.most_common()
                        if freq == max_freq])
        # repition times of group * number of elements in group + number of
        # most frequent tasks that occurs in the end 
        # -> 3*4+2 = (4-1)*(3+1)+2
        # place each most frequent in the last group so there are max_freq-1
        # former groups
        # number of elements in group = n+1
        # add number of most frequent back
        return max((max_freq-1)*(n+1)+max_nmbr, len(tasks))
        # the computation result may < len(tasks), while len(tasks) is minimum


class Solution_Buildup:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        The main function get cnt and schedule for tasks.

        Parameters:
            tasks (list): a list of items.

        Returns:
            cnt (int): integer to track count of items in schedule.
        """
        if n == 0:
            print(tasks)
            return len(tasks)

        # Logic: to minimize the cnt of steps needed, we need to
        # build groups of items of n + 1 tasks to avoide cooldown steps.
        # The most frequent tasks are most relevant and other tasks can be
        # used as seperartors between repeting to be most frequent tasks.
        # Only if we can not seperate most frequent tasks with less frequent
        # tasks, do we use cooldown steps.
        # e.g.
        # tasks ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'D', 'E']
        # with n = 3 can be grouped e.g.
        # schedule = ['A', 'B', 'C', 'D',  'A', 'B', 'C', 'E'
        #             'A', 'B', 'cool', 'cool',  'A', 'B']
        # we only use cool steps once we are out of less frequent tasks and
        # add the most frequent task to the end.
        # 
        cnt = 0
        schedule = []

        counter = self._counter(tasks)
        freq_list = self._sort_by_frequency(counter)
        most_freq_keys, less_freq_keys, highest_freq =\
            self._get_most_and_less_frequent_keys(freq_list)

        # loop until only 1 itemis left in the high highest_freq
        for i in range(0, highest_freq - 1):
            # add most_freq_keys
            group_cnt = 0
            counter, group_cnt, schedule, cnt =\
                self._add_to_schedule(most_freq_keys, counter, group_cnt,
                                      schedule, cnt)

            while group_cnt < n + 1:
                # if items in group are less than n +1,
                # start adding less_freq_keys
                counter, group_cnt, schedule, cnt =\
                    self._add_to_schedule(less_freq_keys, counter, group_cnt,
                                          schedule, cnt)
                # if items in group are less than n +1,
                # add an cool slot
                if group_cnt < n + 1:
                    schedule.append('cool')
                    group_cnt += 1
                    cnt += 1

        # once only 1 itemis left in the high highest_freqm add it (them)
        counter, group_cnt, schedule, cnt =\
            self._add_to_schedule(most_freq_keys, counter, 0,
                                  schedule, cnt)
        print(schedule)
        return cnt

    def _counter(self, arr: list) -> dict:
        """
        The function to count occurances of items in arr.

        Parameters:
            arr (list): a list of items

        Returns:
            counter (dict): a dict with items as key and occurance count as value
        """
        counter = {}
        for val in arr:
            if val in counter:
                counter[val] += 1
            else:
                counter[val] = 1
        return counter

    def _sort_by_frequency(self, counter: dict) -> list:
        """
        The function to sort dict by value

        Parameters:
            counter (dict): a occurance count counter dict

        Returns:
            counter (dict): a dict with items as key and occurance count as
            value and sorted by value
        """
        return sorted(counter.items(),
                      key=lambda kv: kv[1],
                      reverse=True)

    def _get_most_and_less_frequent_keys(self, freq_list: list) -> tuple:
        """
        The function to get the highset frequency, list of high and low
        frequency items

        Parameters:
            freq_list (list of tuples): containing key and occurance
            frequency pairs

        Returns:
            most_freq_keys, less_freq_keys, highest_freq (list, list, int):
            list of items that have the highest occurance frequency, list
            of items that have the not the higest occurance frequency and
            the highest_freq itself.
        """
        highest_freq = freq_list[0][1]
        most_freq_keys = []
        less_freq_keys = []
        for val, cnt in freq_list:
            if cnt == highest_freq:
                most_freq_keys.append(val)
            else:
                less_freq_keys.append(val)
        return most_freq_keys, less_freq_keys, highest_freq

    def _add_to_schedule(self, x_freq_keys: list, counter: dict,
                         group_cnt: int, schedule: list, cnt: int) -> tuple:
        """
        The function to add items to the schedule while reducing items from
        the counter dict. 

        Parameters:
            x_freq_keys (list): a list of dict keys to loop over.
            counter (dict): a dict with items as key and occurance count as
            value and sorted by value.
            group_cnt (int): integer to track count of items in group so far
            schedule (list): scheduled items so far
            cnt (int): integer to track count of items in schedule so far

        Returns:
            updated versions of counter, group_cnt, schedule and cnt.
        """
        for key in x_freq_keys:
            if group_cnt == n + 1:
                break
            if counter[key] > 0:
                schedule.append(key)
                counter[key] -= 1
                group_cnt += 1
                cnt += 1
        return counter, group_cnt, schedule, cnt


print('----')
print()
S1 = Solution_Buildup()
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
exp = 8
print(S1.leastInterval(tasks, n) == exp)

tasks = ["A", "A", "A", "B", "B", "B"]
n = 0
exp = 6
print(S1.leastInterval(tasks, n) == exp)

tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
exp = 16
print(S1.leastInterval(tasks, n) == exp)

tasks = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'D', 'E']
n = 3
exp = 14
print(S1.leastInterval(tasks, n) == exp)


S1 = Solution_Equasion()
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
exp = 8
print(S1.leastInterval(tasks, n) == exp)

tasks = ["A", "A", "A", "B", "B", "B"]
n = 0
exp = 6
print(S1.leastInterval(tasks, n) == exp)

tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
exp = 16
print(S1.leastInterval(tasks, n) == exp)

tasks = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'D', 'E']
n = 3
exp = 14
print(S1.leastInterval(tasks, n) == exp)
